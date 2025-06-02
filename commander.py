# commander.py

from mcp.mcp_protocol import MCPServer, create_message
from agents.bourne import handle_bourne
from agents.bond import handle_bond
from agents.hunt import handle_hunt

def run_mission():
    mcp = MCPServer()

    # Register agents
    mcp.register_agent("Bourne", handle_bourne)
    mcp.register_agent("Bond", handle_bond)
    mcp.register_agent("Hunt", handle_hunt)

    # Step 1: Ask Bourne to fetch papers
    bourne_prompt = [
        create_message("system", "You are Agent Bourne. Fetch the latest LLM papers from arXiv."),
        create_message("user", "Please fetch LLM papers from the past 7 days.")
    ]
    bourne_reply = mcp.send("Bourne", bourne_prompt)
    paper_data = bourne_reply["content"]

    if isinstance(paper_data, str) or "papers" not in paper_data:
        return {"error": "No papers retrieved."}

    papers = paper_data["papers"]

    # Step 2: Send papers to Bond for summarization and code demo
    paper_text = "\n\n".join([
        f"Title: {p['title']}\nAbstract: {p['summary']}" for p in papers
    ])
    bond_prompt = [
        create_message("system", "You are Agent Bond. Summarize LLM papers and create simple code demos."),
        create_message("user", f"Here are some papers:\n\n{paper_text}")
    ]
    bond_reply = mcp.send("Bond", bond_prompt)

    # Step 3: Ask Hunt to extract citations
    hunt_prompt = [
        create_message("system", "You are Agent Hunt. Generate citation strings for academic papers."),
        create_message("user", {"papers": papers})
    ]
    hunt_reply = mcp.send("Hunt", hunt_prompt)

    return {
        "summaries": bond_reply["content"],
        "citations": hunt_reply["content"]
    }
