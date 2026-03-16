# 🤖 Zoro – Python AI Voice Assistant

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)
![Status](https://img.shields.io/badge/Project-Active-success)

**Zoro** is a Python-based **AI voice assistant** that listens to voice commands and performs automated tasks such as opening websites, playing music, fetching news, and answering general questions using a **local AI model**.

The project demonstrates how to integrate **speech recognition, text-to-speech, automation, and local large language models** into a single assistant application.

Zoro can run **partially offline** by using a **local AI model through Ollama**, making it faster and more private than cloud-only assistants.

---

# 🎥 Example Interaction

```
User: Zoro
Assistant: Yes?

User: Open YouTube
Assistant: Opening YouTube
```

---

# ✨ Features

### 🎤 Voice Command Recognition

Converts speech to text using **SpeechRecognition**.

### 🔊 Voice Responses

Zoro speaks responses using **Google Text-to-Speech (gTTS)**.

### 🌐 Website Automation

Open common websites using simple voice commands.

Examples:

* Open Google
* Open YouTube
* Open Instagram
* Open LinkedIn

### 🎵 Music Playback

Play songs using a local **music library file**.

### 📰 News Updates

Fetch the latest news headlines using **News API**.

### 🧠 AI Question Answering

Zoro can answer general questions using a **local AI model**.

### ⚡ Local AI Model Support

Uses **Ollama** to run a local language model instead of relying on paid APIs.

---

# 🏗️ Architecture

Zoro follows a simple **voice assistant pipeline**:

```
Microphone Input
        ↓
Speech Recognition
        ↓
Wake Word Detection (Zoro)
        ↓
Command Processing
        ↓
Task Execution / AI Query
        ↓
Voice Response
```

---

# ⚙️ Technologies Used

| Technology        | Purpose                         |
| ----------------- | ------------------------------- |
| Python            | Core programming language       |
| SpeechRecognition | Convert speech to text          |
| gTTS              | Text-to-speech voice generation |
| PyAudio           | Microphone input                |
| Requests          | API communication               |
| Pygame            | Audio playback                  |
| Ollama            | Run local AI models             |
| Webbrowser        | Open websites                   |

---

# 🧠 AI Integration (Local LLM)

Zoro can answer **general questions using a local AI model** powered by **Ollama**.

Example interaction:

User:

```
Zoro, what is artificial intelligence?
```

Assistant:

```
Artificial Intelligence is a field of computer science that focuses on building systems capable of performing tasks that normally require human intelligence.
```

---

# ⚙️ Setup Ollama

Install **Ollama**

https://ollama.com

After installing, pull a lightweight model:

```
ollama pull qwen2.5:0.5b
```

Make sure Ollama is running before starting Zoro.

Zoro will send user queries to the local model and speak the response.

---

# 🔒 Why Use Local AI?

Using a local AI model provides:

* 🛜 Offline AI responses
* 🔐 Better privacy
* ⚡ Faster responses
* 💰 No API cost

This allows Zoro to behave more like a **true personal AI assistant**.

---

# 📂 Project Structure

```
zoro-ai-assistant
│
├── main.py              # Main assistant logic
├── client.py            # AI interaction handler
├── musicLibrary.py      # Song database
│
├── .env                 # Environment variables (API keys)
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

# 📦 Installation

## 1️⃣ Clone the repository

```
git clone https://github.com/your-username/zoro-ai-assistant.git
cd zoro-ai-assistant
```

---

## 2️⃣ Create a virtual environment (recommended)

```
python -m venv venv
```

Activate the environment

### Windows

```
venv\Scripts\activate
```

### Mac / Linux

```
source venv/bin/activate
```

---

## 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

If **PyAudio fails on Windows**, install it using:

```
pip install pipwin
pipwin install pyaudio
```

---

# ▶️ Running the Assistant

Run the assistant using:

```
python main.py
```

Make sure:

* Your **microphone is connected**
* **Ollama server is running**

---

# 📌 Example Commands

Zoro currently supports commands like:

* Open Google
* Open YouTube
* Open Instagram
* Open LinkedIn
* Play music
* Get news updates
* Ask general questions

---

# 🧠 How It Works

1. The assistant continuously listens for audio input.
2. SpeechRecognition converts the audio into text.
3. Zoro detects the wake word **"Zoro"**.
4. The command is processed.
5. If it matches a predefined command, Zoro executes the task.
6. Otherwise, the query is sent to the **local AI model**.
7. The generated response is spoken back to the user.

---

# 🔮 Future Improvements

Possible upgrades for the assistant:

* 🌦 Weather information
* 📅 Date and time commands
* 🎙 Better wake-word detection
* 🧠 Conversation memory
* 🖥 Desktop GUI interface
* 🔍 Voice-based web search

---

# 🎯 Purpose of This Project

This project was built to:

* Practice **Python automation**
* Learn **speech recognition systems**
* Build a **voice-controlled AI assistant**
* Integrate **local AI models with Python**


