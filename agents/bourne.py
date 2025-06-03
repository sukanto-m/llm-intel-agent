# agents/bourne.py

import os
from openai import OpenAI
from mcp.mcp_protocol import create_message
from utils.fetch_papers import fetch_llm_papers

# Load OpenAI API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def handle_bourne(messages=None):
    if messages is None:
        papers = fetch_llm_papers(max_results=15, days_back=30)

        if not papers:
            return create_message("assistant", "❌ Bourne found no recent LLM papers.")

        prompt = "Summarize these LLM papers in plain English:\n\n"
        for i, paper in enumerate(papers, start=1):
            prompt += f"{i}. {paper['title']}\n{paper['summary']}\nLink: {paper['link']}\n\n"

        messages = [
            {"role": "system", "content": "You are Bourne, an elite AI summarizer of cutting-edge LLM research."},
            {"role": "user", "content": prompt}
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
