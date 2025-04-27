from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS

from langchain_openai import OpenAIEmbeddings

from config.config import inited_config as config

documents = [
    Document(
        page_content="White color (Белый цвет)",
        metadata={"secret": "123"}
    ),
    Document(
        page_content="Black color (Черный цвет)",
        metadata={"secret": "456"}
    ),
    Document(
        page_content="Red color (Красный цвет)",
        metadata={"secret": "789"}
    ),
    Document(
        page_content="Blue color (Синий цвет)",
        metadata={"secret": "321"}
    ),
    Document(
        page_content="Green color (Зеленый цвет)",
        metadata={"secret": "654"}
    ),
    Document(
        page_content="Yellow color (Желтый цвет)",
        metadata={"secret": "987"}
    ),
    Document(
        page_content="Orange color (Оранжевый цвет)",
        metadata={"secret": "147"}
    ),
    Document(
        page_content="Purple color (Фиолетовый цвет)",
        metadata={"secret": "258"}
    ),
    Document(
        page_content="Brown color (Коричневый цвет)",
        metadata={"secret": "741"}
    ),
]

embeddings = OpenAIEmbeddings(api_key=config.openai.api_key)


color_store = FAISS.from_documents(documents, embedding=embeddings)
