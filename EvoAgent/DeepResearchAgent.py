from typing import Any, Optional, Union

from autogen.agentchat.conversable_agent import ConversableAgent
from EvoAgent.DeepResearchTools import DeepResearchTool
import os



#os._exit(0)
__all__ = ["DeepResearchAgent"]


class DeepResearchAgent(ConversableAgent):
    """An agent that performs deep research tasks."""

    DEFAULT_PROMPT = "You are a deep research agent. You have the ability to get information from the web and perform research tasks."

    def __init__(
        self,
        name: str,
        llm_config: dict[str, Any],
        system_message: Optional[Union[str, list[str]]] = DEFAULT_PROMPT,
        max_web_steps: int = 30,
        **kwargs: Any,
    ) -> None:
        """Initialize the DeepResearchAgent.

        Args:
            name (str): The name of the agent.
            llm_config (dict[str, Any]): The LLM configuration.
            system_message (Optional[Union[str, list[str]], optional): The system message. Defaults to DEFAULT_PROMPT.
            max_web_steps (int, optional): The maximum number of web steps. Defaults to 30.
        """
        super().__init__(
            name=name,
            system_message=system_message,
            llm_config=llm_config,
            **kwargs,
        )

        self.tool = DeepResearchTool(
            llm_config=llm_config,
            max_web_steps=max_web_steps,
        )

        self.register_for_llm()(self.tool)
