
import os
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
from core.abstract_component import AbstractComponent
from dotenv import load_dotenv
import yaml

# Input and Output Data Models
class Gpt3SummarizerOutput(BaseModel):
    summary: str


class HtmlSummarizerOutputModel(BaseModel):
    concatenated_summary: str


class SummaryConcatenator(AbstractComponent):
    def __init__(self) -> None:
        super().__init__()
        with open(self.component_configuration_path(), "r", encoding="utf-8") as file:
            yaml_data = yaml.safe_load(file)
        self.concatenation_separator: str = yaml_data["parameters"]["concatenation_separator"]

    def transform(self, input_list: List[Gpt3SummarizerOutput]) -> HtmlSummarizerOutputModel:
        concatenated_summary = ""
        for idx, item in enumerate(input_list):
            concatenated_summary += item.summary
            if idx < len(input_list) - 1:
                concatenated_summary += self.concatenation_separator
        return HtmlSummarizerOutputModel(concatenated_summary=concatenated_summary)

load_dotenv()
SummaryConcatenator_app = FastAPI()

@SummaryConcatenator_app.post("/transform/")
async def transform(input_list: List[Gpt3SummarizerOutput]) -> HtmlSummarizerOutputModel:
    summary_concat = SummaryConcatenator()
    return summary_concat.transform(input_list)
