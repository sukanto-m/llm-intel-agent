# secrets_check.py

import os
from dotenv import load_dotenv

# Load from .env only if not already in environment (fallback for local dev)
if not os.getenv("OPENAI_API_KEY") or not os.getenv("TELEGRAM_BOT_TOKEN"):
    load_dotenv()

def check_required_env_vars(required_vars):
    """Check that all required environment variables are set."""
    missing = [var for var in required_vars if not os.getenv(var)]
    if missing:
        raise EnvironmentError(f"❌ Missing required environment variables: {', '.join(missing)}")
