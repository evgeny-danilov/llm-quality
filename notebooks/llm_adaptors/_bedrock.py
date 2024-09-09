import boto3
from dotenv import load_dotenv, find_dotenv

from langchain_aws import ChatBedrock, BedrockEmbeddings

load_dotenv(find_dotenv())


class BedrockAdapter:
    def __init__(self, model: str, temperature: float = 0):
        self.model = model
        self.temperature = temperature
        self.client = boto3.client(service_name="bedrock-runtime", region_name='us-east-1', verify=False)

    def llm(self, callbacks, streaming=False):
        return ChatBedrock(
            client=self.client,
            model_id=self.model,
            model_kwargs={'temperature': self.temperature, 'max_tokens': 100000},
            streaming=streaming,
            callbacks=callbacks,
        )

    def embeddings(self):
        return BedrockEmbeddings(
            client=self.client,
            model_id=self.model
        )
