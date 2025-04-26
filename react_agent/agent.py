from typing import List

from langchain_openai import ChatOpenAI
from langchain.tools import BaseTool
from langchain_community.tools.tavily_search.tool import TavilySearchResults
from langchain.schema import SystemMessage
from langgraph.prebuilt import create_react_agent


# 1. Инициализация LLM-модели
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# 3. Определяем системный промпт
system_prompt = SystemMessage(
    content=(
        "Вы — ReAct-агент, который может выполнять поиск по интернету "
        "Твои инструменты: 1.TavilySearch - Используй его для поиска по интернету"  # noqa: E501
    )
)

# 4. Инициализация инструментов
tavily_tool = TavilySearchResults(max_results=4)
tools: List[BaseTool] = [tavily_tool]

# 5. Создание агента с системным промптом
graph = create_react_agent(
    model=llm,
    tools=tools,
    prompt=system_prompt
)

# 6. Вызов агента
user_input = "What is the weather in Tokyo?"
inputs = {
    "messages": [
        ("system", system_prompt.content),
        ("user", user_input)
    ]
}
