# agents/bond.py

import os
from openai import OpenAI
from mcp.mcp_protocol import create_message
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(override=True)

# Get the API key
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise EnvironmentError("❌ OPENAI_API_KEY not found in environment or .env file.")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

def handle_bond(messages):
    """
    Uses OpenAI ChatCompletion to summarize LLM papers and suggest code demos.
    Expects messages like:
    - system: your role is Bond, an AI summarizer and code demo generator
    - user: summarize the following paper ...
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4",  # or "gpt-3.5-turbo"
            messages=messages,
            temperature=0.7,
            max_tokens=800
        )
        content = response.choices[0].message.content
        return create_message("assistant", content)

    except Exception as e:
        return create_message("assistant", f"❌ Bond encountered an error: {e}")
