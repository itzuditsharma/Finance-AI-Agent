# Finance AI Agent

## Overview
The **Finance AI Agent** is a powerful AI-driven tool designed to provide financial insights and web search capabilities. It leverages **Phi Agents**, **Groq's LLaMA3-70B model**, and **tool integrations** like YFinance and DuckDuckGo to fetch stock data, analyst recommendations, and company news while also enabling web searches with sources included.

## Features
- **Financial Data Analysis**: Fetch stock prices, analyst recommendations, fundamental stock data, and company news using YFinance.
- **Web Search Capability**: Search for relevant financial and general information using DuckDuckGo.
- **Interactive Chat Interface**: Engage with AI agents in a conversational interface.
- **Dynamic Visualizations**: Present financial data using tables and visual elements for better insights.
- **Multi-Agent Architecture**: Two specialized agents for finance and web search tasks.

## Tech Stack
- **Programming Language**: Python
- **AI Models**: Groq (LLaMA3-70B-8192)
- **Tools Used**:
  - `phi.agent.Agent`: Defines AI agents.
  - `phi.model.groq.Groq`: Utilizes LLaMA3-70B model.
  - `phi.tools.yfinance.YFinanceTools`: Fetches stock-related data.
  - `phi.tools.duckduckgo.DuckDuckGo`: Enables web search.
  - `phi.playground.Playground`: Provides an interactive UI.
- **Environment Variables**: Uses `.env` file for API key management.
- **Server Framework**: `phi.playground.serve_playground_app` for hosting the application.

## Installation & Setup
1. **Clone the Repository:**
   ```sh
   git clone https://github.com/itzuditsharma/Finance-AI-Agent.git
   cd Finance-AI-Agent
   ```
2. **Create a Virtual Environment (Optional but Recommended):**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Install Dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Set Up Environment Variables:**
   - Create a `.env` file in the project directory.
   - Add your Phi API key:
     ```
     PHI_API_KEY=your_api_key_here
     ```
5. **Run the Application:**
   ```sh
   python main.py
   ```
6. **Access the Application:**
   - The Playground UI will be available at `http://localhost:5000`.

## Code Breakdown
### Importing Required Modules
```python
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import phi.api
import os
from dotenv import load_dotenv
from phi.playground import Playground, serve_playground_app
```
- Loads required modules, including AI models, tools, and environment configurations.

### Setting API Key
```python
load_dotenv()
phi.api = os.getenv("PHI_API_KEY")
```
- Reads the Phi API key from the `.env` file.

### Defining AI Agents
#### Web Search Agent
```python
web_search_agent = Agent(
    name = "Web Search Agent",
    role = "Search the web for information",
    model = Groq(id = "llama3-70b-8192"),
    tools = [DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True
)
```
- Uses DuckDuckGo for retrieving web-based information.
- Ensures sources are included in search results.

#### Finance AI Agent
```python
finance_agent = Agent(
    name = "Finance AI Agent",
    role = "Get financial Data",
    model = Groq(id = "llama3-70b-8192"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True)],
    instructions=["Use tables and visualizations for displaying the data"],
    show_tool_calls=True,
    markdown=True
)
```
- Retrieves financial data such as stock prices and company fundamentals using YFinance.
- Formats data using tables and visualizations.

### Initializing Playground UI
```python
app = Playground(agents = [finance_agent, web_search_agent]).get_app()
```
- Creates an interactive AI-driven web application.

### Running the Application
```python
if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)
```
- Starts the server and hosts the application.

### Results
![image](https://github.com/user-attachments/assets/b06b571f-09c7-45a8-93c1-01a78daef722)
![image](https://github.com/user-attachments/assets/8079e36f-24ab-4eee-9de9-a696e05cd631)
![image](https://github.com/user-attachments/assets/5f6795d1-b8f0-49b6-8896-dfda6192a55e)
![image](https://github.com/user-attachments/assets/80977479-167f-48f3-98c6-5c819418788e)
![image](https://github.com/user-attachments/assets/ef1edad4-9390-4484-ba13-6f73fb91be9c)




## Usage
1. **Run the application** and open the web interface.
2. **Interact with the Finance AI Agent** to get stock prices, company news, and financial insights.
3. **Use the Web Search Agent** to find relevant web-based information.
4. **View results in a structured and visual format** using tables and charts.

## Future Enhancements
- **Real-time stock alerts**: Notify users of stock price changes.
- **Sentiment analysis**: Gauge market sentiment from news articles.
- **Portfolio tracking**: Allow users to track investments.
- **Custom model fine-tuning**: Improve response accuracy with domain-specific data.

## License
This project is licensed under the MIT License.

## Contributing
We welcome contributions! Feel free to submit issues and pull requests.


