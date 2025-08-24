# 🕉️ Ganesha's Blessings AI Chatbot

*A Submission for the Ganesh Chaturthi Challenge*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Welcome to Ganesha's Blessings, an interactive AI booth where technology meets tradition. Share your worries, doubts, or challenges with a wise AI inspired by Lord Ganesha, and receive comforting advice rooted in ancient philosophy.

![Ganesha Chatbot Screenshot](...) 
<!-- Pro-Tip: Take a nice screenshot of your app and upload it to your GitHub repo, then replace the "..." with the link to the image -->

---

### ✨ Key Features

*   **🎙️ Voice Interaction:** Speak your worries naturally in your preferred language.
*   **🧠 Philosophical AI:** The chatbot understands your problems and generates wise, comforting responses based on Lord Ganesha's philosophies.
*   **🌐 Multi-Language Support:** Interact in English, Hindi, Tamil, Telugu, Kannada, and Spanish. The chatbot listens and responds in your chosen language.
*   **🗣️ Audio Response:** Hear Ganesha's wisdom spoken back to you in a calm, reassuring voice.
*   **📜 Chat History:** Your conversation is displayed on-screen, creating a continuous chat experience.

---

### 🛠️ Tech Stack

*   **Frontend:** [Streamlit](https://streamlit.io/)
*   **Voice Input:** `streamlit-audiorec`
*   **AI Models (LLM & STT):** [Groq](https://groq.com/) (Llama-3 & Whisper)
*   **Translation:** `deep-translator`
*   **Text-to-Speech:** `gTTS` (Google Text-to-Speech)
*   **Containerization:** [Docker](https://www.docker.com/)

---

### 🚀 Getting Started

There are two ways to run this project: locally using a Python virtual environment or with Docker for a more isolated setup.

#### A. Local Setup (Recommended for Development)

**Prerequisites:**
*   Python 3.9+
*   Git

**Instructions:**

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/[Your-GitHub-Username]/[Your-Repo-Name].git
    cd [Your-Repo-Name]
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For Windows
    python -m venv venv
    .\venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Set up your API key:**
    *   Copy the example environment file: `cp .env.example .env`
    *   Open the newly created `.env` file and add your Groq API key:
      ```
      GROQ_API_KEY="your_actual_groq_api_key_here"
      ```

4.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```
    Your browser should open to the application automatically.

#### B. Docker Setup (Recommended for Production/Easy Deployment)

**Prerequisites:**
*   Docker Desktop

**Instructions:**

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/[Your-GitHub-Username]/[Your-Repo-Name].git
    cd [Your-Repo-Name]
    ```

2.  **Set up your API key:**
    *   Copy the example environment file: `cp .env.example .env`
    *   Open the newly created `.env` file and add your Groq API key.

3.  **Build the Docker image:**
    ```bash
    docker build -t ganesha-chatbot .
    ```

4.  **Run the Docker container:**
    ```bash
    docker run --rm -p 8501:8501 --env-file .env ganesha-chatbot
    ```
    Open your browser and navigate to `http://localhost:8501`.

---

### 📜 Usage

1.  Select your preferred language from the dropdown menu.
2.  Click the microphone icon to start recording your message.
3.  Click the icon again to stop recording.
4.  Wait a few moments as Ganesha transcribes, contemplates, and responds.
5.  The response will be displayed as text and played as audio.
