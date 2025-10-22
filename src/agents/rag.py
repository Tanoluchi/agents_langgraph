from langgraph.graph import MessagesState
from langchain_core.messages import AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
file_search_tool = {
    "type": "file_search",
    "vector_store_ids": ["my_course_docs"],
}
llm = llm.bind_tools([file_search_tool])

class State(MessagesState):
    customer_name: str
    my_age: int
    

def node_1(state: State):
    new_state: State = {}
    if state.get("customer_name") is None:
        new_state["customer_name"] = "John Doe"
    else: 
        new_state["my_age"] = 30
        
    history = state["messages"]
    last_message = history[-1]
    ai_message = llm.invoke(last_message.content)
    new_state["messages"] = [ai_message]
    return new_state


from langgraph.graph import StateGraph, START, END

builder = StateGraph(State)
builder.add_node("node1", node_1)

builder.add_edge(START, "node1")
builder.add_edge("node1", END)

agent = builder.compile()

