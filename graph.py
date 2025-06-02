# graph.py
from langgraph.graph import StateGraph
from nodes.bourne import bourne_node
from nodes.bond import bond_node
from nodes.hunt import hunt_node
from nodes.powers import powers_node

def build_graph():
    builder = StateGraph()

    builder.add_node("Bourne", bourne_node)
    builder.add_node("Bond", bond_node)
    builder.add_node("Hunt", hunt_node)
    builder.add_node("Powers", powers_node)

    builder.set_entry_point("Bourne")
    builder.add_edge("Bourne", "Bond")
    builder.add_edge("Bourne", "Hunt")
    builder.add_edge("Bond", "Powers")
    builder.add_edge("Hunt", "Powers")
    builder.set_finish_point("Powers")

    return builder.compile()
