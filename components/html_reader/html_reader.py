
import os
import requests
from typing import Optional
import yaml
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

from core.abstract_component import AbstractComponent

class HtmlReaderInputDict(BaseModel):
    url: str

class HtmlReaderOutputDict(BaseModel):
    html_content: str

class HtmlReader(AbstractComponent):
    def __init__(self) -> None:
        super().__init__()
        with open(self.component_configuration_path(), "r", encoding="utf-8") as file:
            yaml_data = yaml.safe_load(file)
        self.user_agent: str = yaml_data["parameters"]["user_agent"]
        self.timeout: int = yaml_data["parameters"]["timeout"]

    def transform(self, args: HtmlReaderInputDict) -> HtmlReaderOutputDict:
        headers = {
            "User-Agent": self.user_agent
        }
        response = requests.get(args.url, headers=headers, timeout=self.timeout)
        html_content = response.text
        return HtmlReaderOutputDict(html_content=html_content)

load_dotenv()
html_reader_app = FastAPI()

@html_reader_app.post("/transform/")
async def transform(args: HtmlReaderInputDict) -> HtmlReaderOutputDict:
    html_reader = HtmlReader()
    return html_reader.transform(args)
