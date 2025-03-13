from typing import Any, Literal, Optional

from . import ConversableAgent
from autogen.tools.experimental import BrowserUseTool, Crawl4AITool
from autogen.tools.tool import Tool



__all__ = ["WebSearchAgent"]

class WebSearchAgent(ConversableAgent):
    """An agent that uses web tools to interact with the web."""

    def __init__(
        self,
        *,
        llm_config: dict[str, Any],
        web_tool_llm_config: Optional[dict[str, Any]] = None,
        web_tool: Literal["browser_use", "crawl4ai"] = "browser_use",
        web_tool_kwargs: Optional[dict[str, Any]] = None,
        **kwargs: Any,
    ) -> None:
        """Initialize the WebSurferAgent.

        Args:
            llm_config (dict[str, Any]): The LLM configuration.
            web_tool_llm_config (dict[str, Any], optional): The LLM configuration for the web tool. I not provided, the llm_config will be used.
            web_tool (Literal["browser_use", "crawl4ai"], optional): The web tool to use. Defaults to "browser_use".
            web_tool_kwargs (dict[str, Any], optional): The keyword arguments for the web tool. Defaults to None.
        """
        web_tool_kwargs = web_tool_kwargs if web_tool_kwargs else {}
        web_tool_llm_config = web_tool_llm_config if web_tool_llm_config else llm_config
        if web_tool == "browser_use":
            self.tool: Tool = BrowserUseTool(llm_config=web_tool_llm_config, **web_tool_kwargs)
        elif web_tool == "crawl4ai":
            self.tool = Crawl4AITool(llm_config=web_tool_llm_config, **web_tool_kwargs)
        else:
            raise ValueError(f"Unsupported {web_tool=}.")

        super().__init__(llm_config=llm_config, **kwargs)

        self.register_for_llm()(self.tool)
