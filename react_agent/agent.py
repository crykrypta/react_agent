from typing import List

from langchain_openai import ChatOpenAI
from langchain.tools import BaseTool
from langchain.schema import SystemMessage
from langgraph.prebuilt import create_react_agent

from react_agent.utils.tools import (  # type: ignore
    tavily_tool,
    get_secret_code_from_color
)


# 1. Инициализация LLM-модели
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# 2. Инициализация инструментов
tools: List[BaseTool] = [tavily_tool, get_secret_code_from_color]

# 3. Определяем системный промпт
system_str = """\
Вы — специальный агент, который должен угадать секретный код
Чтобы угадать секретный код, ты должен будешь сначала угадать цвет, который имеет в виду пользователь.

Если вопрос понятен, например "Какого цвета небо?"
- ты можешь сразу попробовать использовать инструмент [get_secret_code_from_color] с аргументом color="blue"

Если тебе нужна дополнительная информация для ответа, например "Какого цвета небо сейчас в Москве?",
- то ты можешь использовать инструмент [tavily_tool] для поиска по интернету,
чтобы узнать погоду и если в Москве пасмурно то аргумент будет color="gray" А если погода ясная то аргумент будет color="blue"

Твои инструменты:
1.tavily_tool - Используй его для поиска по интернету
2.get_secret_code_from_color - Используй его для получения секретного кода из цвета, который ты угадал.
"""  # noqa: E501

system_prompt = SystemMessage(content=system_str)


# 4. Создание агента
graph = create_react_agent(
    model=llm,
    tools=tools,
    prompt=system_prompt
)

# 5. Вызов агента
user_input = "What is the weather in Tokyo?"
inputs = {
    "messages": [
        ("system", system_prompt.content),
        ("user", user_input)
    ]
}
