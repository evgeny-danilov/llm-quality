import os

from langchain_openai import AzureChatOpenAI, AzureOpenAIEmbeddings
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(usecwd=True))


class AzureGptAdaptor:
    def __init__(self, model: str, temperature: float = 0):
        self.model = model
        self.temperature = temperature
        self.openai_api_version = "2023-09-01-preview"

    def llm(self, callbacks, streaming=False):
        return AzureChatOpenAI(
            azure_endpoint=os.environ["OPENAI_API_ENDPOINT"],
            api_key=os.environ["OPENAI_API_KEY"],
            openai_api_version=self.openai_api_version,
            azure_deployment=self.model,
            temperature=self.temperature,
            streaming=streaming,
            callbacks=callbacks,
        )

    def embeddings(self):
        return AzureOpenAIEmbeddings(
            openai_api_version=self.openai_api_version,
            azure_deployment=self.model
        )
