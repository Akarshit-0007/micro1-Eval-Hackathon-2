from langgraph.graph import START, END, StateGraph
from model.state import OverAllState
from nodes.load_dataset_node import load_dataset_node
from nodes.llm_with_internal_files import llm_with_internal_files
from nodes.llm_without_internal_files import llm_without_internal_files

def route_within_files(state: OverAllState):
    if state.contain_files == True:
        return "llm_with_internal_files"
    else:
        return "llm_without_internal_files"

# Use OverAllState instead of dict
workflow = StateGraph(OverAllState)

# 1. Add the nodes
workflow.add_node("load_dataset_node", load_dataset_node)
workflow.add_node("llm_with_internal_files", llm_with_internal_files)
workflow.add_node("llm_without_internal_files", llm_without_internal_files)

# 2. Use the string name in the edges
workflow.add_edge(START, "load_dataset_node")
workflow.add_conditional_edges(
    "load_dataset_node",
    route_within_files,
    {
        "llm_with_internal_files": "llm_with_internal_files",
        "llm_without_internal_files": "llm_without_internal_files"
    }
)
workflow.add_edge("llm_with_internal_files", END)
workflow.add_edge("llm_without_internal_files", END)

app = workflow.compile()

# Generate and save the graph visualization
png_data = app.get_graph().draw_mermaid_png()

with open("graph.png", "wb") as f:
    f.write(png_data)
print("Graph saved as graph.png")

print(app)