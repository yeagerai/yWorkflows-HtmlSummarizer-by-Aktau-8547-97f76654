
import os
from typing import List
import yaml
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
import openai

from core.abstract_component import AbstractComponent


class Gpt3SummarizerInputDict(BaseModel):
    text_chunks: List[str]


class Gpt3SummarizerOutputDict(BaseModel):
    summaries: List[str]


class Gpt3Summarizer(AbstractComponent):
    def __init__(self) -> None:
        super().__init__()
        with open(self.component_configuration_path(), "r", encoding="utf-8") as file:
            yaml_data = yaml.safe_load(file)
        self.api_key: Optional[str] = os.environ.get(
            yaml_data["parameters"]["api_key"]
        )
        self.engine: str = yaml_data["parameters"]["engine"]
        self.temperature: float = yaml_data["parameters"]["temperature"]
        self.max_tokens: int = yaml_data["parameters"]["max_tokens"]

    def transform(
        self, args: Gpt3SummarizerInputDict
    ) -> Gpt3SummarizerOutputDict:
        openai.api_key = self.api_key
        summaries = []

        for chunk in args.text_chunks:
            response = openai.Completion.create(
                engine=self.engine,
                prompt=chunk,
                temperature=self.temperature,
                max_tokens=self.max_tokens,
            )
            summary = response.choices[0].text
            summaries.append(summary.strip())

        return Gpt3SummarizerOutputDict(summaries=summaries)


load_dotenv()
gpt3_summarizer_app = FastAPI()


@gpt3_summarizer_app.post("/transform/")
async def transform(
    args: Gpt3SummarizerInputDict,
) -> Gpt3SummarizerOutputDict:
    gpt3_summarizer = Gpt3Summarizer()
    return gpt3_summarizer.transform(args)
