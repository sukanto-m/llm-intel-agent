# agents/bourne.py

import os
from openai import OpenAI
from mcp.mcp_protocol import create_message
from utils.fetch_papers import fetch_llm_papers

# Load OpenAI API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def handle_bourne(messages=None):
    """
    Agent Bourne builds its own messages unless provided externally.
    """
    if messages is None:
        # Build messages internally
        papers = fetch_llm_papers(max_results=10, days_back=7)

        if not papers:
            return create_message("assistant", "❌ Bourne found no recent LLM papers.")

        summary_prompt = "Summarize the following papers:\n\n"
        for i, paper in enumerate(papers, start=1):
            summary_prompt += f"{i}. {paper['title']}\n{paper['summary']}\nLink: {paper['link']}\n\n"

        messages = [
            {"role": "system", "content": "You are Bourne, an elite AI summarizer."},
            {"role": "user", "content": summary_prompt}
        ]

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            temperature=0.7,
            max_tokens=1200
        )
        content = response.choices[0].message.content
        return create_message("assistant", content)

    except Exception as e:
        return create_message("assistant", f"❌ Bourne failed: {e}")