# agents/bourne.py

import feedparser
from mcp.mcp_protocol import create_message

def handle_bourne(messages):
    latest_msg = [m for m in messages if m["role"] == "user"][-1]
    
    if "LLM papers" not in latest_msg["content"]:
        return create_message("assistant", "Sorry, I only fetch LLM papers from arXiv.")

    feed = feedparser.parse("http://export.arxiv.org/api/query?search_query=all:LLM&start=0&max_results=5")
    papers = []
    for entry in feed.entries:
        papers.append({
            "title": entry.title,
            "link": entry.link,
            "summary": entry.summary,
            "authors": [a.name for a in entry.authors]
        })

    # Return papers inside the assistant message
    return create_message("assistant", {
        "papers": papers,
        "note": f"Fetched {len(papers)} LLM papers from arXiv."
    })
