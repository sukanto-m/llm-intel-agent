# mcp/mcp_protocol.py

class MCPServer:
    def __init__(self):
        self.agents = {}
        self.history = []

    def register_agent(self, name, handler):
        self.agents[name] = handler

    def send(self, agent_name, messages):
        """Send message list to agent and store in history."""
        self.history.append({"to": agent_name, "messages": messages})
        response = self.agents[agent_name](messages)
        self.history.append({"from": agent_name, "messages": [response]})
        return response

    def get_history(self):
        return self.history


def create_message(role, content):
    return {"role": role, "content": content}
