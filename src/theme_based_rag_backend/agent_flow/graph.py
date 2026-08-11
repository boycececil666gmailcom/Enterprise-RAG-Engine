from langgraph.graph import StateGraph, END
from src.theme_based_rag_backend.agent_flow.state import AgentState, InputState
from src.theme_based_rag_backend.agent_flow.nodes import (
    classifier_node,
    hyde_decision_node,
    hyde_node,
    rag_qa_node,
    refuse_node,
    critique_node
)
from src.theme_based_rag_backend.agent_flow.edges import (
    route_by_category,
    route_by_hyde_decision,
    route_after_critique
)

# Workflow Graph Setup
workflow = StateGraph(AgentState, input=InputState)

# Add Nodes
workflow.add_node("classifier", classifier_node)
workflow.add_node("hyde_decision", hyde_decision_node)
workflow.add_node("hyde", hyde_node)
workflow.add_node("rag_qa", rag_qa_node)
workflow.add_node("refuse", refuse_node)
workflow.add_node("critique", critique_node)

# Set Entry Point and Edges
workflow.set_entry_point("classifier")

workflow.add_conditional_edges(
    "classifier",
    route_by_category,
    {
        "rag": "hyde_decision",
        "refuse": "refuse"
    }
)

workflow.add_conditional_edges(
    "hyde_decision",
    route_by_hyde_decision,
    {
        "enable": "hyde",
        "skip": "rag_qa"
    }
)

workflow.add_edge("hyde", "rag_qa")
workflow.add_edge("rag_qa", "critique")
workflow.add_edge("refuse", "critique")

workflow.add_conditional_edges(
    "critique",
    route_after_critique,
    {
        "approved": END,
        "rejected": "classifier"  # Loop back to the start (Classifier Node)
    }
)

# Compile Workflow Graph
agent_graph = workflow.compile()
