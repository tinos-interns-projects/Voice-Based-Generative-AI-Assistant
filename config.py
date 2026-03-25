# Configuration settings for the voice assistant
import os

from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

# Speech Recognition Settings
RECOGNIZER_PHRASE_TIME_LIMIT = 10  # seconds
RECOGNIZER_PAUSE_THRESHOLD = 0.8  # seconds

# Text-to-Speech Settings
TTS_RATE = 150  # Words per minute
TTS_VOLUME = 0.9  # Volume level (0.0 to 1.0)

# Logging
LOG_LEVEL = "INFO"
LOG_FILE = "logs/assistant.log"

# Conversation Settings
MAX_CONVERSATION_HISTORY = 10  # Number of exchanges to remember
