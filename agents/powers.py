# nodes/powers.py

def powers_node(state):
    summaries = state.get("summaries", [])
    citations = state.get("citations", [])

    lines = ["# 🧠 LLM Intelligence Dossier with Code Demos\n"]
    for i, s in enumerate(summaries):
        lines.append(f"## {s['title']}\n")
        lines.append(f"{s['summary']}\n")
        if i < len(citations):
            lines.append(f"📌 Citation: {citations[i]['citation']}")
        lines.append("### 🔧 Code Demo:\n")
        lines.append("```python\n" + s['demo_code'].strip() + "\n```")
        lines.append("---\n")

    state["report"] = "\n".join(lines)
    return state