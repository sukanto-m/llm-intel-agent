# agents/bourne.py

import os
from openai import OpenAI
from mcp.mcp_protocol import create_message
from utils.fetch_papers import fetch_llm_papers

# Load OpenAI API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def handle_bourne():
    """
    Agent Bourne:
    - Fetches recent LLM-related papers from arXiv
    - Summarizes them via OpenAI
    - Returns a single assistant message with all summaries
    """

    papers = fetch_llm_papers(max_results=10, days_back=7)

    if not papers:
        return create_message("assistant", "❌ Bourne found no recent LLM papers.")

    # Prepare a message for the LLM
    summary_prompt = "Summarize the following papers in plain English:\n\n"
    for i, paper in enumerate(papers, start=1):
        summary_prompt += f"{i}. {paper['title']}\n{paper['summary']}\nLink: {paper['link']}\n\n"

    messages = [
        {"role": "system", "content": "You are Bourne, an elite AI summarizer. Keep it crisp and clear."},
        {"role": "user", "content": summary_prompt}
    ]

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=messages,
            temperature=0.7,
            max_tokens=1200
        )
        content = response.choices[0].message.content
        return create_message("assistant", content)

    except Exception as e:
        return create_message("assistant", f"❌ Bourne failed: {e}")
