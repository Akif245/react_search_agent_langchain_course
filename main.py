# from dotenv import load_dotenv


# load_dotenv()
from dotenv import load_dotenv
load_dotenv()

import os

print(os.getenv("OPENAI_API_KEY"))
import importlib
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
# from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI

try:
    tavily_module = importlib.import_module("tavily")
    TavilyClient = getattr(tavily_module, "TavilyClient")
except ImportError as exc:
    raise ImportError("tavily package is required to run this script. Install it via pip install tavily") from exc

tavily = TavilyClient()

@tool
def search(query: str) -> str:
    """
    Tool that searches over internet
    Args:
        query: The query to search for
    Returns:
        The search result
    """
    print(f"Searching for {query}")
    return tavily.search(query=query)


# llm = ChatOpenAI(model="gpt-5")
# tools = [search]
# agent = create_agent(model=llm,tools=tools)

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

tools = [search]
agent = create_agent(model=llm, tools=tools)

def main():
    print("Hello from langchain-course1")
    result = agent.invoke({"messages":HumanMessage(content="search for 3 job postings for an ai engineer using langchain in the bay area on linkedin and list their details")})
    print(result)

if __name__ == "__main__":
    main()  