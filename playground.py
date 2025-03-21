from phi.agent import Agent 
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import phi.api
import os
import phi
from phi.playground import Playground, serve_playground_app

from dotenv import load_dotenv
load_dotenv()

phi.api = os.getenv("PHI_API_KEY")

# Web Search Agent 
web_search_agent = Agent(
    name = "Web Search Agent",
    role = "Search the web for information",
    model = Groq(id = "llama3-70b-8192"), 
    tools = [DuckDuckGo()],
    instructions= ["Always include sources"],
    show_tool_calls=True,
    markdown=True
)

finance_agent = Agent(
    name = "Finance AI Agent",
    role = "Get financial Data",
    model = Groq(id = "llama3-70b-8192"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True)],
    instructions=["Use tables and visualizations for displaying the data"],
    show_tool_calls=True,
    markdown=True
)

app = Playground(agents = [finance_agent, web_search_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)

