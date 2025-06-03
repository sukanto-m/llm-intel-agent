# mcp/mcp_protocol.py

class MCPServer:
    def __init__(self):
        self.agents = {}
        self.history = []

    def register_agent(self, name, handler):
        self.agents[name] = handler

    def send(self, agent_name, messages=None):
        """
        Sends a message to the specified agent.
        If `messages` is None, the agent is expected to self-initialize.
        """
        if agent_name not in self.agents:
            return create_message("assistant", f"❌ Unknown agent: {agent_name}")

        try:
            return self.agents[agent_name](messages)
        except Exception as e:
            return create_message("assistant", f"❌ Agent '{agent_name}' failed: {e}")


    def get_history(self):
        return self.history


def create_message(role, content):
    return {"role": role, "content": content}
