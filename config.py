import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Get value from .env
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL = os.getenv("MODEL", "gpt-4o-mini")
MAX_TOKENS = int(os.getenv("MAX_TOKENS", 1024))
TEMPERATURE = float(os.getenv("TEMPERATURE", 0.7))

if not OPENAI_API_KEY:
        raise ValueError("OPENAI_API_KEY not in .env file defined")