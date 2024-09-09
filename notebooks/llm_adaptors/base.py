import json
import pdb

from langchain_core.runnables import RunnableLambda

from ._azure_gpt import AzureGptAdaptor
from ._bedrock import BedrockAdapter
from .models import LlmModels as BaseModels
from langchain_core.output_parsers import BaseOutputParser

class BaseLlmAdaptor:
    def __init__(self, model: str, temperature: float = 0):
        self.model = model
        if model.startswith('gpt'):
            self.adapter = AzureGptAdaptor(model=model, temperature=temperature)
        else:
            self.adapter = BedrockAdapter(model=model, temperature=temperature)

    def llm(self, callbacks=[], streaming=False):
        callbacks = callbacks.copy()
        return RunnableLambda(lambda x: self.adapter.llm(callbacks=callbacks, streaming=streaming).invoke(x))

    def async_llm(self, callbacks=[]):
        return self.llm(callbacks=callbacks, streaming=True)

    def embeddings(self):
        return self.adapter.embeddings()


class BaseJsonParser:
    def parse(self, input_text: str) -> dict:
        extracted_text = self._extract_text(input_text)
        return self._parse_json(extracted_text)

    def _extract_text(self, input_text: str) -> str:
        if hasattr(input_text, 'content'):
            input_text = input_text.content
        elif hasattr(input_text, 'page_content'):
            input_text = input_text.page_content
        elif not hasattr(input_text, 'find'):
            return ''
        start_index = input_text.find("{")
        end_index = input_text.rfind("}")
        if start_index != -1 and end_index != -1:
            return input_text[start_index:end_index + 1]
        return ""

    def _parse_json(self, extracted_text: str) -> dict:
        try:
            json_data = json.loads(extracted_text, strict=False)
            if json_data.get('properties', None):
                return json_data['properties']
            else:
                return json_data
        except json.JSONDecodeError as e:
            print(e)
            return DefaultDict()


class DefaultDict(dict):
    def __missing__(self, key):
        return 'incorrect json output'
