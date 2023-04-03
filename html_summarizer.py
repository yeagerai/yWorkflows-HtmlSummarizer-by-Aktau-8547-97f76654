
import typing
from typing import Optional
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

from core.workflows.abstract_workflow import AbstractWorkflow

load_dotenv()

class HtmlSummarizerIn(BaseModel):
    url: str


class HtmlSummarizerOut(BaseModel):
    summary: str


class HtmlSummarizer(AbstractWorkflow):
    def __init__(self) -> None:
        super().__init__()
        self.description = "A component that takes a URL as input and outputs a summary of the retrieved HTML content. The component fetches the HTML content from the provided URL, parses and extracts the significant text, and generates a concise summary that represents the main information contained in the original HTML."

    async def transform(
        self, args: HtmlSummarizerIn, callbacks: typing.Any
    ) -> HtmlSummarizerOut:
        results_dict = await super().transform(args=args, callbacks=callbacks)
        summary = results_dict["summary"].text
        out = HtmlSummarizerOut(summary=summary)
        return out

html_summarizer_app = FastAPI()

@html_summarizer_app.post("/transform/")
async def transform(
    args: HtmlSummarizerIn,
) -> HtmlSummarizerOut:
    html_summarizer = HtmlSummarizer()
    return await html_summarizer.transform(args, callbacks=None)

