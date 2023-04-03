
import os
from typing import List

import yaml
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

from core.abstract_component import AbstractComponent


class HtmlParserInputDict(BaseModel):
    html_content: str


class HtmlParserOutputDict(BaseModel):
    parsed_text: str


class HtmlParser(AbstractComponent):
    def __init__(self) -> None:
        super().__init__()
        with open(self.component_configuration_path(), "r", encoding="utf-8") as file:
            yaml_data = yaml.safe_load(file)
        self.tags_to_extract: List[str] = yaml_data["parameters"]["tags_to_extract"]

    def transform(
        self, args: HtmlParserInputDict
    ) -> HtmlParserOutputDict:
        soup = BeautifulSoup(args.html_content, "html.parser")
        parsed_text = ""

        for tag in self.tags_to_extract:
            elements = soup.find_all(tag)
            for element in elements:
                parsed_text += element.text + "\n"

        return HtmlParserOutputDict(parsed_text=parsed_text)


load_dotenv()
html_parser_app = FastAPI()


@html_parser_app.post("/transform/")
async def transform(
    args: HtmlParserInputDict,
) -> HtmlParserOutputDict:
    html_parser = HtmlParser()
    return html_parser.transform(args)
