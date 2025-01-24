
import os
from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI
from dotenv import load_dotenv
from tools.calculator_tool import get_calculator_tool

# Load environment variables from .env file
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Ensure the API key is loaded
if not OPENAI_API_KEY:
    raise ValueError("Please set your OpenAI API key in the .env file")

# Initialize the language model
llm = OpenAI(model="text-davinci-003", temperature=0.7, openai_api_key=OPENAI_API_KEY)

def add_func(a,b):
    return(a+b)
    
def sub(a,b):
    return (git a-b)

# Load tools
calculator_tool = get_calculator_tool()
tools = [
    Tool(
        name=calculator_tool["name"],
        func=calculator_tool["func"],
        description=calculator_tool["description"],
    )
]

# Initialize the agent
agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

# Main script to interact with the agent
if __name__ == "__main__":
    print("Agentic AI is ready! Type 'quit' to exit.")
    while True:
        try:
            query = input("You: ")
            if query.lower() == "quit":
                print("Goodbye!")
                break
            response = agent.run(query)
            print(f"Agent: {response}")
        except Exception as e:
            print(f"Error: {e}")
