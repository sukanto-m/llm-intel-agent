import os
from openai import OpenAI
from mcp.mcp_protocol import create_message

# No dotenv, no fallback
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def handle_bond(messages):
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            temperature=0.7,
            max_tokens=800
        )
        content = response.choices[0].message.content
        return create_message("assistant", content)
    except Exception as e:
        return create_message("assistant", f"❌ Bond failed: {e}")
