from dotenv import load_dotenv
load_dotenv()
import os

from EvoAgent.WebSearch import WebSearchAgent

llm_config = {
    "config_list": 
    [
        {
            #"api_type": "openai", 
            "model": "gpt-4o",
            "base_url": os.environ["OPENAI_BASE_URL"],
            "api_key": os.environ["OPENAI_API_KEY"]
        }
    ]
}
# 2. Add additional browser configurations for our browser-use tool
browser_use_browser_config ={
    "browser_config": {"headless": False},
    "agent_kwargs": {"generate_gif": True}
}

# 3. Create the agent, nominating the tool and tool config
web_researcher = WebSearchAgent(
    name="researcher",
    llm_config=llm_config,
    web_tool="browser_use",
    web_tool_kwargs=browser_use_browser_config,
    )

# 4. Run our agent, passing in the tools that our WebSurferAgent has so they can be executed
ag2_news_result = web_researcher.run(
    "Search for the latest news of Donald Trump",
    tools=web_researcher.tools,
)

print(ag2_news_result.summary)