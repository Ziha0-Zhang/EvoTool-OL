from dotenv import load_dotenv
load_dotenv()


import os

from autogen import AssistantAgent, UserProxyAgent
from autogen.tools.experimental import Crawl4AITool, BrowserUseTool



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
user_proxy = UserProxyAgent(name="user_proxy", human_input_mode="NEVER")
assistant = AssistantAgent(name="assistant", llm_config=llm_config)
tool_name = "browser"
if tool_name == "browser":
    
    browser_use_tool = BrowserUseTool(
        llm_config=llm_config,
        browser_config={"headless": False},
    )
    browser_use_tool.register_for_execution(user_proxy)
    browser_use_tool.register_for_llm(assistant)

else:
    crawlai_tool = Crawl4AITool(llm_config=llm_config)
    crawlai_tool.register_for_execution(user_proxy)
    crawlai_tool.register_for_llm(assistant)

web_url = "https://www.currentaffairs.org/news/will-democrats-keep-protecting-abusive-men"
query_message = f"Get information of {web_url}"
print(query_message)
result = user_proxy.initiate_chat(
    recipient=assistant,
    message=query_message,
    max_turns=3,
)