import os
from dotenv import load_dotenv

# Load from .env file
load_dotenv()

# Read keys
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
CALORIES_NINJA_KEY = os.getenv("CALORIES_NINJA_KEY")

# Model name
GEMINI_MODEL = "gemini-1.5-flash"
