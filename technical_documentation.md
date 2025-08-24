# Ganesha's Blessings AI - Technical Documentation

## 1. Project Overview

This project is an interactive, voice-based AI chatbot designed for the Ganesh Chaturthi Challenge. It provides a unique blend of technology and tradition, allowing users to share their worries with an AI modeled after Lord Ganesha. The chatbot listens in multiple languages, processes the user's problem, and offers comforting, philosophical advice inspired by Ganesha's stories and wisdom.

## 2. System Architecture: The "Ganesha's Magical Booth"

The system is designed as a modular web application. An intuitive way to understand the architecture is to imagine it as a real festival booth:

*   **The Booth's Operator (Frontend - Streamlit):** The entire user interface is built with Streamlit. It's responsible for displaying all visual elements (title, language selector, chat history) and managing user interactions. Its main job is to coordinate all the other components.

*   **The Magical Microphone (Voice Input - `streamlit-audiorec`):** This component captures the user's voice directly in the browser. It's lightweight and pure Python, avoiding complex system dependencies like `ffmpeg`.

*   **The High-Speed Messenger (API Client - `groq-python`):** This is the bridge to the powerful AI models in the cloud. It takes data from our application and securely sends it to the Groq API endpoints.

*   **The All-Knowing Sage (AI Models - Groq Cloud):**
    *   **Speech-to-Text (`Whisper-large-v3`):** When the messenger delivers an audio file, this model transcribes it into text with high accuracy, supporting multiple languages.
    *   **Core Logic (`Llama-3-8b`):** When the messenger delivers text, this Large Language Model processes it. It is guided by a carefully crafted **System Prompt** that instructs it to adopt the persona of Lord Ganesha—wise, calm, and philosophical.

*   **The Universal Translator (Translation - `deep-translator`):** This component acts as a bridge for the sage, who only speaks English. It translates the user's native language to English for the LLM, and then translates the LLM's English response back to the user's language.

*   **The Voice Synthesizer (Text-to-Speech - `gTTS`):** This machine takes the final, translated text and converts it into an audio file, using the correct language pronunciation.

*   **The Perfect Workshop (Deployment - Docker):** The entire application is containerized using Docker. This solves the "it works on my machine" problem by packaging the application, all its Python and system dependencies (`build-essential`, `portaudio19-dev`), and the correct Python version into a single, portable image. This guarantees that the application runs identically everywhere.

## 3. Workflow / Data Flow

A single user interaction follows these steps:

1.  The user selects a language in the Streamlit UI.
2.  The user records their voice using the `streamlit-audiorec` widget.
3.  The raw audio bytes are sent to the `app.py` script.
4.  The script sends these audio bytes to the Groq Whisper API for transcription.
5.  The transcribed text is received (e.g., in Hindi).
6.  The `deep-translator` library translates the Hindi text to English.
7.  The English text, along with the Ganesha persona prompt, is sent to the Groq Llama-3 API.
8.  The LLM generates a philosophical response in English.
9.  The `deep-translator` library translates the English response back to Hindi.
10. The `gTTS` library converts the final Hindi text into an MP3 audio stream.
11. Streamlit displays the text response and automatically plays the audio response to the user.
12. The conversation is saved in `st.session_state` to persist the chat history.

## 4. Tools, APIs, and Models Used

*   **Python 3.11:** Core programming language.
*   **Streamlit:** Web application framework.
*   **Docker:** Containerization and deployment.
*   **Groq API:**
    *   `llama3-8b-8192`: For generating philosophical responses.
    *   `whisper-large-v3`: For multi-lingual speech-to-text.
*   **Libraries:**
    *   `streamlit-audiorec`: For ffmpeg-free audio recording.
    *   `deep-translator`: For reliable and conflict-free language translation.
    *   `gTTS`: For simple and effective text-to-speech.
    *   `python-dotenv`: For managing API keys securely.
