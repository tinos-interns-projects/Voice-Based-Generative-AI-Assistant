# 🎙️ Voice-Based Generative AI Assistant

<div align="center">

![Voice Assistant](https://img.shields.io/badge/Voice%20Enabled-AI%20Chatbot-blue?style=for-the-badge&logo=openai)
![Python](https://img.shields.io/badge/Python-3.9+-green?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-red?style=for-the-badge&logo=flask)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

### 🚀 A Smart, Voice-Enabled AI Chatbot for Seamless Conversations

> Transform your words into intelligent conversations with cutting-edge AI technology

</div>

---

## ✨ Features

<table>
  <tr>
    <td align="center" width="33%">
      <h3>🎙️ Voice Recognition</h3>
      <p>Speak naturally and let the AI understand you perfectly with OpenAI Whisper</p>
    </td>
    <td align="center" width="33%">
      <h3>🧠 Intelligent Responses</h3>
      <p>Powered by Google Gemini for context-aware, thoughtful answers</p>
    </td>
    <td align="center" width="33%">
      <h3>🔊 Voice Output</h3>
      <p>Listen to AI responses with natural text-to-speech technology</p>
    </td>
  </tr>
  <tr>
    <td align="center" width="33%">
      <h3>💾 Chat Memory</h3>
      <p>SQLite database remembers your conversations automatically</p>
    </td>
    <td align="center" width="33%">
      <h3>📱 Web Interface</h3>
      <p>Clean, intuitive Flask-based dashboard for easy interaction</p>
    </td>
    <td align="center" width="33%">
      <h3>🔄 Conversation History</h3>
      <p>Review and continue past conversations anytime</p>
    </td>
  </tr>
</table>

---

## 🎯 What Does This Project Do?

```
┌─────────────────────────────────────────────────────┐
│  You Speak  →  AI Listens  →  AI Thinks  →  AI Talks │
│     🗣️      →      👂     →      🧠      →      🔊    │
└─────────────────────────────────────────────────────┘
```

This intelligent assistant combines **three powerful technologies**:

1. **🎵 OpenAI Whisper** - Converts your voice to text with high accuracy
2. **🤖 Google Gemini** - Generates intelligent, contextual responses  
3. **🔊 Text-to-Speech (pyttsx3)** - Speaks responses back to you naturally
4. **💾 SQLite Database** - Saves all conversations for later review

**Perfect for:**
- 📚 Learning companions
- 🏢 Business automation
- ♿ Accessibility tools
- 🎮 Interactive applications

---

## 📊 Project Architecture

```
Voice-Based-Generative-AI-Assistant/
│
├── 📄 app.py                 ← Main Flask application
├── ⚙️ config.py              ← Configuration & API keys
├── 📋 requirements.txt       ← Python dependencies
├── 🔑 .env.example           ← Environment variables template
│
├── 📁 utils/                 ← Utility modules
│   ├── llm.py               ← Language model interface (Google Gemini)
│   └── stt.py               ← Speech-to-text module (Whisper)
│
├── 📁 templates/            ← HTML templates
│   └── index.html           ← Web UI dashboard
│
├── 📁 static/               ← CSS, JavaScript, assets
│
├── 📁 tests/                ← Unit tests
│
├── 📁 logs/                 ← Application logs
│   └── assistant.log
│
└── 📁 flask_session/        ← Session management
```

---

## 🛠️ Technology Stack

<div align="center">

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Frontend** | HTML5, CSS3, JavaScript | Web interface & user interactions |
| **Backend** | Python 3.9+ | Core application logic |
| **Framework** | Flask | Web server & routing |
| **AI/ML** | Google Gemini API | Intelligent responses |
| **Speech Recognition** | OpenAI Whisper | Voice-to-text conversion |
| **Text-to-Speech** | pyttsx3 | Audio output |
| **Database** | SQLite | Chat history storage |
| **Session Management** | Flask-Session | User session handling |
| **Deployment** | Gunicorn | Production server |

</div>

---

## ⚡ Quick Start

### 📋 Prerequisites

Make sure you have installed:
- **Python 3.9** or higher
- **pip** (Python package manager)
- **FFmpeg** (for audio processing)
- **Microphone** (for voice input)

### 🚀 Installation Steps

#### **Step 1: Clone the Repository**
```bash
git clone https://github.com/muhammedmuflih/Voice-Based-Generative-AI-Assistant.git
cd Voice-Based-Generative-AI-Assistant
```

#### **Step 2: Create Virtual Environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

#### **Step 3: Install Dependencies**
```bash
pip install -r requirements.txt
```

#### **Step 4: Set Up Environment Variables**

Create a `.env` file in the project root:

```env
# Google Gemini API
GEMINI_API_KEY=your_google_gemini_api_key_here
GEMINI_MODEL=gemini-2.5-flash

# OpenAI API (for Whisper)
OPENAI_API_KEY=your_openai_api_key_here

# Logging
LOG_LEVEL=INFO
LOG_FILE=logs/assistant.log
```

**Get Your API Keys:**
- 🔑 [Google Gemini API Key](https://makersuite.google.com/app/apikey)
- 🔑 [OpenAI API Key](https://platform.openai.com/api-keys)

#### **Step 5: Validate API Keys**
```bash
python validate_api.py
```

#### **Step 6: Run the Application**
```bash
python app.py
```

#### **Step 7: Open in Browser**
Navigate to: `http://localhost:5000` 🌐

---

## 📖 API Endpoints

### **Chat Endpoints**

#### **1️⃣ Send Text Message**
```http
POST /chat
Content-Type: application/json

{
  "message": "Your message here"
}
```
**Response:**
```json
{
  "response": "AI's response",
  "status": "success",
  "chat_id": 1
}
```

#### **2️⃣ Send Voice Input**
```http
POST /voice
Content-Type: multipart/form-data

audio_data: <audio.webm>
```
**Response:**
```json
{
  "response": "AI's response",
  "status": "success",
  "transcription": "What you said"
}
```

#### **3️⃣ Start New Chat**
```http
POST /new_chat
```

#### **4️⃣ Get Chat History**
```http
GET /history
```
**Response:**
```json
{
  "chats": [
    {
      "id": 1,
      "title": "First message...",
      "created_at": "2026-03-25 10:00:00"
    }
  ]
}
```

#### **5️⃣ Load Specific Chat**
```http
GET /history/<chat_id>
```

#### **6️⃣ Delete Chat**
```http
DELETE /delete_chat/<chat_id>
```

#### **7️⃣ Clear Conversation**
```http
POST /clear
```

---

## ⚙️ Configuration Guide

### **config.py Parameters**

```python
# Speech Recognition
RECOGNIZER_PHRASE_TIME_LIMIT = 10      # Max recording time (seconds)
RECOGNIZER_PAUSE_THRESHOLD = 0.8       # Pause detection (seconds)

# Text-to-Speech
TTS_RATE = 150                          # Speed (words per minute)
TTS_VOLUME = 0.9                        # Volume (0.0 to 1.0)

# AI Model
GEMINI_MODEL = "gemini-2.5-flash"       # Google Gemini model

# Conversation Memory
MAX_CONVERSATION_HISTORY = 10           # Number of exchanges to remember
```

### **Fine-Tuning Tips** 🎚️

| Parameter | Increase | Decrease |
|-----------|----------|----------|
| `PHRASE_TIME_LIMIT` | Allow longer pauses in speech | Recognize speech faster |
| `PAUSE_THRESHOLD` | More lenient with silence | Stricter silence detection |
| `TTS_RATE` | Slower speech | Faster speech |
| `TTS_VOLUME` | Louder output | Quieter output |

---

## 🗄️ Database Schema

### **Conversations Table**
```sql
CREATE TABLE conversations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    created_at TIMESTAMP
);
```

### **Messages Table**
```sql
CREATE TABLE messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    conversation_id INTEGER,
    sender TEXT,                    -- 'user' or 'assistant'
    content TEXT,
    timestamp TIMESTAMP,
    FOREIGN KEY(conversation_id) REFERENCES conversations(id)
);
```

---

## 🔐 Security Best Practices

✅ **Implemented:**
- Environment variables for sensitive data
- Session management with Flask-Session
- Input validation on all endpoints
- Error handling and logging
- Automatic temp file cleanup

⚠️ **Recommendations:**
- Use HTTPS in production
- Implement rate limiting
- Add authentication/authorization
- Use secure session storage (Redis/Database)
- Validate audio file formats
- Add CORS restrictions

---

## 📝 Code Examples

### **Example 1: Simple Chat**
```python
import requests

response = requests.post('http://localhost:5000/chat', 
    json={"message": "What's the weather like?"})

print(response.json()['response'])
# Output: "I don't have real-time weather data, but you can check..."
```

### **Example 2: Get Conversation History**
```python
import requests

chats = requests.get('http://localhost:5000/history').json()

for chat in chats['chats']:
    print(f"Chat {chat['id']}: {chat['title']}")
    print(f"Created: {chat['created_at']}\n")
```

### **Example 3: Send Voice Input**
```python
import requests

files = {'audio_data': open('voice.webm', 'rb')}
response = requests.post('http://localhost:5000/voice', files=files)

data = response.json()
print(f"You said: {data['transcription']}")
print(f"AI says: {data['response']}")
```

---

## 🐛 Troubleshooting

### **Problem: "No module named 'google.generativeai'"**
```bash
pip install google-generativeai==0.3.2
```

### **Problem: "Error: Microphone not found"**
- Check microphone is connected
- Verify audio drivers are installed
- Try: `python -c "import speech_recognition; sr.Microphone()"`

### **Problem: "GEMINI_API_KEY not found"**
- Create `.env` file with your key
- Make sure `python-dotenv` is installed
- Verify file is in project root

### **Problem: "Database is locked"**
- Close all previous Flask instances
- Delete `chat_history.db`
- Restart the application

### **Problem: "Port 5000 already in use"**
```bash
# Change port in app.py
app.run(debug=True, host='0.0.0.0', port=5001)
```

---

## 📚 Dependencies Explained

| Package | Version | Purpose |
|---------|---------|---------|
| `google-generativeai` | 0.3.2 | Google Gemini API client |
| `SpeechRecognition` | 3.10.0 | Speech-to-text wrapper |
| `pyttsx3` | 2.90 | Text-to-speech engine |
| `pyaudio` | 0.2.11 | Audio input/output |
| `python-dotenv` | 1.0.0 | Environment variables |
| `flask` | Latest | Web framework |
| `flask-session` | Latest | Session management |
| `openai-whisper` | Latest | Advanced STT |
| `gunicorn` | Latest | Production server |

---

## 🚀 Deployment

### **Deploy to Heroku**
```bash
# Create Procfile
echo "web: gunicorn app:app" > Procfile

# Deploy
git push heroku main
```

### **Deploy to PythonAnywhere**
1. Upload files to PythonAnywhere
2. Create virtual environment
3. Set up WSGI configuration
4. Point to your app

### **Docker Deployment**
```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "app:app"]
```

---

## 📊 Performance Tips

- **Caching:** Implement Redis for session caching
- **Database:** Add indexes to frequently queried columns
- **API Calls:** Implement request batching
- **Frontend:** Use lazy loading for chat history
- **Audio:** Compress audio before transmission

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** changes (`git commit -m 'Add amazing feature'`)
4. **Push** to branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### **Areas for Improvement:**
- [ ] Add more language support
- [ ] Implement user authentication
- [ ] Add analytics dashboard
- [ ] Support for multiple voices
- [ ] Conversation export (PDF/JSON)
- [ ] Mobile app integration
- [ ] Advanced NLP features

---

## 🎓 Learning Resources

- 📖 [Flask Documentation](https://flask.palletsprojects.com/)
- 🧠 [Google Gemini API Guide](https://ai.google.dev/)
- 🎵 [OpenAI Whisper Docs](https://github.com/openai/whisper)
- 🔊 [pyttsx3 Documentation](https://pyttsx3.readthedocs.io/)
- 💾 [SQLite Tutorial](https://www.sqlite.org/docs.html)

---

## 📞 Support & Contact

Having issues? Need help?

- 🐛 [Report a Bug](https://github.com/muhammedmuflih/Voice-Based-Generative-AI-Assistant/issues)
- 💬 [Start a Discussion](https://github.com/muhammedmuflih/Voice-Based-Generative-AI-Assistant/discussions)
- 📧 Contact: muhammedmuflih@github.com

---

## 📜 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

You are free to:
- ✅ Use commercially
- ✅ Modify the code
- ✅ Distribute copies
- ✅ Use privately

---

## 🌟 Show Your Support

If you find this project helpful:
- ⭐ **Star the repository**
- 🍴 **Fork it for your own use**
- 📣 **Share with others**
- 🐛 **Report bugs and suggest features**

---

## 🙏 Acknowledgments

Thanks to:
- 🤖 **Google** for Gemini API
- 🎵 **OpenAI** for Whisper
- 🔊 **pyttsx3 Contributors** for TTS
- 🌐 **Flask Community** for the amazing framework

---

<div align="center">

### 🎉 Built with ❤️ by Muhammed Muflih & Gabriel

**A Collaborative Effort | Teamwork Makes Dreams Work**

---

#### 👥 **Meet the Team:**

| Developer | Role | Contribution |
|-----------|------|--------------|
| **Muhammed Muflih** | Lead Developer | Architecture, Backend, AI Integration |
| **Gabriel** | Co-Developer | Frontend, Voice Processing, UI/UX |

---

**Made with Python | Powered by AI | Enhanced by Technology**

![Python](https://img.shields.io/badge/Made%20with-Python-blue?logo=python&logoColor=white)
![Love](https://img.shields.io/badge/Made%20with-%E2%9D%A4-red)

**Last Updated:** March 2026

</div>

---

## 📈 Project Statistics

```
📊 Quick Facts:
├── 🐍 Language: Python 3.9+
├── 📦 Dependencies: 10 packages
├── 💾 Database: SQLite
├── 🌐 Frontend: HTML/CSS/JS
├── 🔌 API: RESTful Flask
├── 🎙️ Voice Input: Whisper
├── 🧠 AI Engine: Gemini
└── 🔊 Voice Output: pyttsx3
```

---

<div align="center">

**[⬆ back to top](#-voice-based-generative-ai-assistant)**

</div>
