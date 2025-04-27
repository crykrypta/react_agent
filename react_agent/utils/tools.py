from typing import Literal

from langchain.tools import tool
from langchain_community.tools.tavily_search.tool import TavilySearchResults
# from vectorstores.colors import color_store  # type: ignore

color_map = {
    "white": "123",
    "black": "456",
    "red": "789",
    "blue": "321",
    "green": "654",
    "gray": "000",
}


@tool
def get_secret_code_from_color(
    query: Literal["white", "black", "red", "blue", "green", "gray"]
) -> str:
    """Use this tool for determining the secret code from the color name
    Args:
        query: The color name
    Returns:
        The secret code of the color

    Advice:
        The user may implicitly hint riddles about the color,
        you have to guess and choose the right one color
    """
    # docs = color_store.similarity_search(query, k=1)

    # color = docs[0].page_content
    # secret_code = docs[0].metadata["secret"]

    color = query.lower()
    secret_code = color_map[color]

    message = f'Color: {color}; Code: {secret_code}'
    return message


tavily_tool = TavilySearchResults(max_results=3)
