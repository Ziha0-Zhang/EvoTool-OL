from dotenv import load_dotenv
load_dotenv()
import os

from EvoAgent.DeepResearchAgent import DeepResearchAgent

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

agent = DeepResearchAgent(
    name="DeepResearchAgent",
    llm_config=llm_config,
)

message = "What blogs has Jina Al published recently, and what are some of her inspirations?"

result = agent.run(
    message=message,
    tools=agent.tools,
    max_turns=2,
    user_input=False,
    summary_method="reflection_with_llm",
)

print(result.summary)