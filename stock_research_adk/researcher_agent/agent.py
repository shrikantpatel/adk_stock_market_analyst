from google.adk.agents import Agent
from google.adk.tools import google_search
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Define your primary researcher agent
root_agent = Agent(
    name="researcher_agent",
    model="gemini-2.0-flash",
    description="An agent that specializes in researching financial news and stock information.",
    instruction="You are a financial researcher. Use the provided tools to find the latest news from credible financial sources to identify promising IPOs and existing stocks.",
    tools=[google_search]
)