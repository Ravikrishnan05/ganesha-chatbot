# Ganesha's Blessings AI - Technical Documentation

## 1. Project Overview

This project is an interactive, voice-based AI chatbot designed for the Ganesh Chaturthi Challenge. It provides a unique blend of technology and tradition, allowing users to share their worries with an AI modeled after Lord Ganesha. The chatbot listens in multiple languages, processes the user's problem, and offers comforting, philosophical advice. The entire application is containerized with Docker to ensure reliability and ease of deployment.

## 2. System Architecture: The "Booth in a Box"

The system is designed as a modular web application. The architecture is best understood through the analogy of a self-contained "booth in a box," where each component has a specific role.

*   **The Booth Operator (Frontend - Streamlit):** The entire user interface and application flow are managed by Streamlit. It handles displaying visual elements, managing user interactions, and coordinating all backend services. `st.session_state` is used to maintain a persistent chat history between user interactions.

*   **The Microphone (Voice Input - `streamlit-audiorec`):** This component was specifically chosen because it captures audio directly in the browser without requiring any complex system dependencies like `ffmpeg`. This simplifies both local setup and the Docker build process.

*   **The Universal Translator (Translation - `deep-translator`):** This library acts as a "translation sandwich." It translates the user's transcribed text from their native language into English for the AI model and then translates the AI's English response back to the user's language. This library was chosen over others because it is actively maintained and avoids the dependency conflicts that can arise with older packages.

*   **The Sages (AI Models - Groq Cloud):**
    *   **The Scribe (`Whisper-large-v3`):** This model performs high-accuracy, multi-lingual speech-to-text, converting the user's audio into written words.
    *   **The Oracle (`Llama-3-8b`):** This Large Language Model is the core "brain." It receives the user's problem in English and, guided by a carefully engineered **System Prompt**, generates a response that embodies the persona of Lord Ganesha—wise, compassionate, and philosophical.

*   **The Voice of Ganesha (Text-to-Speech - `gTTS`):** This library takes the final translated text and converts it into a natural-sounding audio file in the correct language, which is then played back to the user.

*   **The Booth in a Box (Deployment - Docker):** The entire application is containerized. The `Dockerfile` defines a minimal, reproducible environment based on `python:3.11-slim`. This solves all dependency issues by packaging the OS, Python, all required libraries, and the application code into a single, portable image. This guarantees that the application runs identically on any machine.

## 3. Workflow / Data Flow

A single user interaction follows these precise steps:

1.  The user selects a language from the `st.selectbox` in the UI.
2.  The user records their voice using `streamlit-audiorec`.
3.  The raw audio bytes are captured and stored in `st.session_state` to prevent re-processing.
4.  The script sends these audio bytes to the **Groq Whisper API** for transcription.
5.  The transcribed text is received (e.g., in Hindi). The user's message is added to the chat history.
6.  `deep-translator` translates the Hindi text to English.
7.  The English text, along with the Ganesha persona prompt, is sent to the **Groq Llama-3 API**.
8.  The LLM generates a philosophical response in English.
9.  `deep-translator` translates the English response back to Hindi.
10. `gTTS` converts the final Hindi text into an MP3 audio stream.
11. The assistant's response (both text and audio) is added to the `st.session_state` chat history.
12. Streamlit re-runs the script, displaying the updated chat history and auto-playing the new audio response.

## 4. Challenges and Debugging Journey

The development process involved overcoming several significant technical hurdles, which were critical to the project's success:

*   **Dependency Conflicts:** Initial attempts with older translation libraries (`googletrans`) caused dependency conflicts with the `groq` library. This was solved by switching to the more modern and compatible `deep-translator` library.
*   **Complex System Dependencies:** Early audio libraries required `ffmpeg` and system build tools (`gcc`, `portaudio-dev`). This complicated the setup. The issue was resolved by finding and implementing `streamlit-audiorec`, a pure-python solution that removed these external dependencies, simplifying the `Dockerfile` and local setup.
*   **Docker Environment Variable Issues:** A major challenge was a `401 Invalid API Key` error that only occurred inside Docker, despite working locally. Through systematic debugging (using `docker run -it ... /bin/sh` and `printenv`), it was discovered that the `.env` file's double quotes were being passed literally by Docker. The solution was to remove the quotes from the `.env` file, resolving the authentication issue. This was a critical lesson in the subtle differences between local and containerized environments.
*   **Streamlit State Management:** Early versions of the app would re-process the same audio on every interaction. This was solved by implementing a robust state management pattern using `st.session_state` to store and clear audio data after it has been processed once.
