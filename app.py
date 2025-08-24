# app.py
import streamlit as st
from st_audiorec import st_audiorec
import os
from groq import Groq
from gtts import gTTS
import io
from dotenv import load_dotenv
from deep_translator import GoogleTranslator

load_dotenv()

# --- Initialize Session State ---
if 'audio_data' not in st.session_state:
    st.session_state.audio_data = None
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# --- FUNCTIONS (Unchanged) ---
def text_to_audio(text, lang='en'):
    try:
        tts = gTTS(text=text, lang=lang, slow=False)
        audio_fp = io.BytesIO()
        tts.write_to_fp(audio_fp)
        audio_fp.seek(0)
        return audio_fp.read()
    except Exception as e:
        st.error(f"Error in text-to-speech conversion: {e}")
        return None

# --- GROQ CLIENT AND PERSONA (Unchanged) ---
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
GANESHA_PERSONA_PROMPT = """
You are Lord Ganesha, the remover of obstacles. You are speaking to a devotee. 
Your personality is wise, compassionate, and calm.
Your responses must be:
1.  Rooted in philosophical wisdom (obstacles are lessons, wisdom over strength, new beginnings).
2.  Short, comforting, and easy to understand (2-3 sentences).
3.  End with a blessing like "Be blessed," or "May your path be clear."
4.  NEVER give medical/financial advice or discuss politics. Gently deflect inappropriate questions.
"""

# --- UI CODE ---
st.set_page_config(layout="centered", page_title="Ganesha's Blessings")
st.title("Ganesha's Blessings 🙏")

# Language Selection (Unchanged)
languages = {
    "English": "en",
    "Hindi": "hi",
    "Tamil": "ta",
    "Telugu": "te",
    "Kannada": "kn",
    "Spanish": "es",
}
selected_language_name = st.selectbox("Choose your language:", list(languages.keys()))
language_code = languages[selected_language_name]

st.write("Speak your worries to Lord Ganesha. Click the microphone to start and stop recording.")

# --- NEW AUDIO HANDLING LOGIC ---
wav_audio_data = st_audiorec()

if wav_audio_data is not None and wav_audio_data != st.session_state.get('last_audio_data', None):
    st.session_state.audio_data = wav_audio_data
    st.session_state.last_audio_data = wav_audio_data
    st.rerun()

# --- Display Chat History ---
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.write(message["content"])
        if "audio" in message:
            st.audio(message["audio"], format="audio/mp3")

# --- PROCESSING LOGIC ---
if st.session_state.audio_data is not None:
    audio_file = io.BytesIO(st.session_state.audio_data)
    audio_file.name = "temp_audio.wav"
    st.session_state.audio_data = None

    with st.spinner("Transcribing your words..."):
        try:
            # Step A: Speech-to-Text
            transcription = client.audio.transcriptions.create(
                file=audio_file,
                model="whisper-large-v3"
            )
            user_text_original_lang = transcription.text

            st.session_state.chat_history.append({"role": "user", "content": f"You said ({selected_language_name}): *{user_text_original_lang}*"})

            if language_code != 'en':
                user_text_english = GoogleTranslator(source='auto', target='en').translate(user_text_original_lang)
            else:
                user_text_english = user_text_original_lang

            with st.spinner("Ganesha is contemplating..."):
                # Step C: Get Ganesha's response in English
                # THIS IS THE CORRECTED LINE:
                chat_completion = client.chat.completions.create(
                    messages=[
                        {"role": "system", "content": GANESHA_PERSONA_PROMPT},
                        {"role": "user", "content": user_text_english}
                    ],
                    model="llama3-8b-8192",
                )
                ganesha_response_english = chat_completion.choices[0].message.content

                if language_code != 'en':
                    ganesha_response_final = GoogleTranslator(source='en', target=language_code).translate(ganesha_response_english)
                else:
                    ganesha_response_final = ganesha_response_english

                audio_output = text_to_audio(ganesha_response_final, lang=language_code)

                st.session_state.chat_history.append({
                    "role": "assistant",
                    "content": f"Ganesha replies ({selected_language_name}): *{ganesha_response_final}*",
                    "audio": audio_output
                })
                
                st.rerun()

        except Exception as e:
            st.error(f"An error occurred: {e}")
            st.session_state.audio_data = None