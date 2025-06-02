# agents/hunt.py

from mcp.mcp_protocol import create_message

def handle_hunt(messages):
    latest_msg = [m for m in messages if m["role"] == "user"][-1]
    papers = latest_msg["content"].get("papers", [])

    if not papers:
        return create_message("assistant", "No papers provided for citation.")

    citations = []
    for p in papers:
        citation = f"{p['authors'][0]} et al., \"{p['title']}\", arXiv, {p['link']}"
        citations.append(citation)

    return create_message("assistant", {
        "citations": citations,
        "note": f"Generated {len(citations)} citations."
    })
