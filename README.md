# 🕉️ Ganesha's Blessings AI Chatbot

*A Submission for the Ganesh Chaturthi Challenge*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Welcome to Ganesha's Blessings, an interactive AI booth where technology meets tradition. Share your worries, doubts, or challenges with a wise AI inspired by Lord Ganesha, and receive comforting advice rooted in ancient philosophy. This application is fully containerized with Docker for easy and reliable deployment.

 
<!-- TODO: Take a nice screenshot of your app, upload it to a site like https://imgur.com/, and replace this link -->

---

### ✨ Key Features

*   **🎙️ Voice Interaction:** Speak your worries naturally in your chosen language.
*   **🧠 Philosophical AI:** The chatbot understands your problems and generates wise, comforting responses based on Lord Ganesha's core philosophies.
*   **🌐 Multi-Language Support:** Interact in English, Hindi, Tamil, Telugu, Kannada, and Spanish. The chatbot listens and responds in your chosen language.
*   **🗣️ Audio Response:** Hear Ganesha's wisdom spoken back to you in a calm, reassuring voice.
*   **📜 Persistent Chat History:** Your entire conversation is displayed on-screen and persists between interactions.

---

### 🛠️ Tech Stack

*   **Frontend:** [Streamlit](https://streamlit.io/)
*   **Voice Input:** `streamlit-audiorec` (A lightweight, `ffmpeg`-free component)
*   **AI Models (LLM & STT):** [Groq](https://groq.com/) (Llama-3 & Whisper)
*   **Translation:** `deep-translator`
*   **Text-to-Speech:** `gTTS` (Google Text-to-Speech)
*   **Containerization:** [Docker](https://www.docker.com/)

---

### 🚀 Getting Started

The recommended way to run this project is with Docker, as it guarantees a perfect, hassle-free setup. A local setup is also provided for development purposes.

#### A. Docker Setup (Recommended for Reliability)

**Prerequisites:**
*   [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running.

**Instructions:**

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/[Your-GitHub-Username]/[Your-Repo-Name].git
    cd [Your-Repo-Name]
    ```

2.  **Set up your API key:**
    *   Create a copy of the example environment file. In your terminal, run: `copy .env.example .env` (on Windows) or `cp .env.example .env` (on macOS/Linux).
    *   Open the newly created `.env` file and add your Groq API key. The file should look like this (without quotes):
      ```
      GROQ_API_KEY=gsk_your_actual_groq_api_key_here
      ```

3.  **Build the Docker image:**
    ```bash
    docker build -t ganesha-chatbot .
    ```

4.  **Run the Docker container:**
    ```bash
    docker run --rm -p 8501:8501 --env-file .env ganesha-chatbot
    ```
    Open your browser and navigate to `http://localhost:8501`.

#### B. Local Setup (For Development)

**Prerequisites:**
*   Python 3.9+
*   Git

**Instructions:**

1.  **Clone the repository and navigate into it.**

2.  **Create and activate a virtual environment:**
    ```bash
    # For Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Set up your API key** as described in the Docker setup (copy `.env.example` to `.env` and add your key).

4.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```

---

### 📜 Usage

1.  Select your preferred language from the dropdown menu.
2.  Click the microphone icon to start recording your message.
3.  Click the icon again to stop recording.
4.  Wait a few moments as Ganesha transcribes, contemplates, and responds.
5.  The response will be added to the chat history and played as audio.

1.  Select your preferred language from the dropdown menu.
2.  Click the microphone icon to start recording your message.
3.  Click the icon again to stop recording.
4.  Wait a few moments as Ganesha transcribes, contemplates, and responds.
5.  The response will be displayed as text and played as audio.
