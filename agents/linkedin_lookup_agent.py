import sys
import os
from dotenv import load_dotenv
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


load_dotenv()

from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import (
    create_react_agent,
    AgentExecutor
)
from langchain import hub
from tools.tools import get_profile_url_tavily

def lookup(name: str) -> str:
    llm = ChatOllama(model="llama3")

    template = """given the full name {name_of_person} I want you to get it me a link to their Linkedin profile page.Your answer should contain only a URL"""
    
    prompt_template = PromptTemplate(
        template=template,
        input_variables=["name_of_person"]
    )
    
    tools_for_agent = [
        Tool(
        name="Crawl Google 4 Linkedin profile page",
        func=get_profile_url_tavily,
        description="useful for when you need to look up LinkedIn Page URL",
    )]

    react_prompt = hub.pull("hwchase17/react")

    agent = create_react_agent(
        llm=llm,
        tools=tools_for_agent,
        prompt=react_prompt,
    )
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True )

    result = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(name_of_person=name)}
    )
    linked_profile_url = result["output"]
    return linked_profile_url
    
if __name__ == "__main__":
    LinkedinUrl = lookup("Muhammad Fariz Ramadhan")
    print(LinkedinUrl)