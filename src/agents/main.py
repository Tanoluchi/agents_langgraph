from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI

@tool
async def get_weather(city: str) -> str:
    """Devuelve el clima para la ciudad dada."""
    return f"It's always sunny in {city}!"


model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
)

agent = create_agent(
    model=model,
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)