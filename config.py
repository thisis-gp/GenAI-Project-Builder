import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Read the Gemini API key from environment variables
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
