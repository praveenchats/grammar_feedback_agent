from langgraph.graph import StateGraph, END
from grammar_feedback_agent import grammar_node

# Build a simple graph with just the grammar node
graph = StateGraph(dict)
graph.add_node("grammar", grammar_node)
graph.set_entry_point("grammar")
graph.add_edge("grammar", END)

# Compile the graph
agent = graph.compile()

# Analyze text
state = {
    "text": "A young engineer working at Ola’s artificial intelligence arm, Krutrim, died by suicide on May 8, allegedly due to extreme work pressure."
}
result = agent.invoke(state)

# Print the feedback
print("Grammar Suggestions:", result.get("grammar", []))