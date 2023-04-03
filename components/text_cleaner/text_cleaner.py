
import os
import re
import html
from typing import Optional
import yaml
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from core.abstract_component import AbstractComponent


class TextCleanerInputDict(BaseModel):
    raw_text: str


class TextCleanerOutputDict(BaseModel):
    cleaned_text: str


class TextCleaner(AbstractComponent):
    def __init__(self) -> None:
        super().__init__()
        with open(self.component_configuration_path(), "r", encoding="utf-8") as file:
            yaml_data = yaml.safe_load(file)
        self.remove_html_entities: bool = yaml_data["parameters"]["remove_html_entities"]
        self.remove_special_characters: bool = yaml_data["parameters"]["remove_special_characters"]

    def transform(
        self, args: TextCleanerInputDict
    ) -> TextCleanerOutputDict:
        print(f"Executing the transform of the {type(self).__name__} component...")

        cleaned_text = " ".join(args.raw_text.split())

        if self.remove_html_entities:
            cleaned_text = html.unescape(cleaned_text)

        if self.remove_special_characters:
            cleaned_text = re.sub(r"[^\w\s]", "", cleaned_text)

        return TextCleanerOutputDict(cleaned_text=cleaned_text)


load_dotenv()
text_cleaner_app = FastAPI()


@text_cleaner_app.post("/transform/")
async def transform(
    args: TextCleanerInputDict,
) -> TextCleanerOutputDict:
    text_cleaner = TextCleaner()
    return text_cleaner.transform(args)
