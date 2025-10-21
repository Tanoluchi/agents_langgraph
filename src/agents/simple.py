from langgraph.graph import MessagesState
from langchain_core.messages import AIMessage

class State(MessagesState):
    customer_name: str
    my_age: int
    

def node_1(state: State):
    history = state["messages"]
    if state.get("customer_name") is None:
        return {"customer_name": "Alice"}
    else: 
        ai_message = AIMessage(content=f"Hello {state.get('customer_name')}, how can I help you today?")
        return {
            "messages": [ai_message]
        }

from langgraph.graph import StateGraph, START, END

builder = StateGraph(State)
builder.add_node("node1", node_1)

builder.add_edge(START, "node1")
builder.add_edge("node1", END)

agent = builder.compile()

