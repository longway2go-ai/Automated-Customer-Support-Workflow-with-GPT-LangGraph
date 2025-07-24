import os
from typing import Optional, Literal
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from openai import OpenAI
from dotenv import load_dotenv
from pydantic import BaseModel
import json

load_dotenv(override=True)
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Define valid query types
QueryType = Literal["order_status", "return_policy", "product_info", "other"]

# Define schema for state tracking
class State(TypedDict):
    user_query: str
    query_type: Optional[QueryType]
    response: Optional[str]

# Step 1: Classify the query
def classify_query(state: State):
    query = state["user_query"]
    SYSTEM_PROMPT = """
    Classify the customer query into one of the following types:
    - order_status
    - return_policy
    - product_info
    - other

    Return JSON like this: {"query_type": "order_status"}
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": query},
        ],
        response_format={"type": "json_object"},
    )
    parsed = json.loads(response.choices[0].message.content)
    state["query_type"] = parsed["query_type"]
    return state

def route_by_type(state: State) -> QueryType:
    return state["query_type"]


def handle_order_status(state: State):
    state["response"] = "You can track your order here: https://store.com/track-order"
    return state

def handle_return_policy(state: State):
    state["response"] = "Our return policy is available here: https://store.com/returns"
    return state

def handle_product_info(state: State):
    state["response"] = "You can browse product details here: https://store.com/products"
    return state

def handle_other(state: State):
    state["response"] = "Thanks for your message. Our support team will get back to you shortly."
    return state

graph_builder = StateGraph(State)
graph_builder.add_node("classify_query", classify_query)
graph_builder.add_node("order_status", handle_order_status)
graph_builder.add_node("return_policy", handle_return_policy)
graph_builder.add_node("product_info", handle_product_info)
graph_builder.add_node("other", handle_other)


graph_builder.add_edge(START, "classify_query")
graph_builder.add_conditional_edges("classify_query", route_by_type)
graph_builder.add_edge("order_status", END)
graph_builder.add_edge("return_policy", END)
graph_builder.add_edge("product_info", END)
graph_builder.add_edge("other", END)


graph = graph_builder.compile()


def main():
    user_input = input(" Customer: ")
    init_state: State = {
        "user_query": user_input,
        "query_type": None,
        "response": None,
    }
    result = graph.invoke(init_state)

    print(" Agent Response:")
    print(f"{result['response']}")
    print(f"(Detected Type: {result['query_type']})")

if __name__ == "__main__":
    main()
