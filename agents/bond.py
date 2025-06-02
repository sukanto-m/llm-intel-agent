# agents/bond.py

import os
from openai import OpenAI
from mcp.mcp_protocol import create_message
from secrets_check import check_required_env_vars

# Ensure required env var is present
check_required_env_vars(["OPENAI_API_KEY"])

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def handle_bond(messages):
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=messages,
            temperature=0.7,
            max_tokens=800
        )
        content = response.choices[0].message.content
        return create_message("assistant", content)
    except Exception as e:
        return create_message("assistant", f"❌ Bond encountered an error: {e}")
