from typing import List

from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import OpenAI, ChatOpenAI
from langchain_tavily import TavilySearch
from langchain.agents.structured_output import ToolStrategy


class Source(BaseModel):
    """Schema for a source used by the agent"""

    url:str = Field(description="The URL of the source")


class AgentResponse(BaseModel):
    """Schema for a response from the agent"""

    answer:str = Field(description="The agent's answer to the query")
    sources:List[Source] = Field(default_factory=list, description="List of sources to generate the answer")

llm = ChatOpenAI(model="gpt-5")
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools, response_format=ToolStrategy(AgentResponse))


def main():
    print("Hello from langchain-course 2")
    result = agent.invoke({"messages":HumanMessage(content="Search for 3 job positions for an AI Engineer using LangChain in Armenia on linkedin and list their details")})
    print(result)

if __name__ == "__main__":
    main()