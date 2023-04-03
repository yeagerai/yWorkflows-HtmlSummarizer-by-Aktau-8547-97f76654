
import os
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
import yaml
import nltk
import spacy

from core.abstract_component import AbstractComponent

class TextChunkerInputDict(BaseModel):
    cleaned_text: str

class TextChunkerOutputDict(BaseModel):
    text_chunks: List[str]

class TextChunker(AbstractComponent):
    def __init__(self) -> None:
        super().__init__()
        with open(self.component_configuration_path(), "r", encoding="utf-8") as file:
            yaml_data = yaml.safe_load(file)
        self.tokenization_library: str = yaml_data["parameters"]["tokenization_library"]
        self.max_token_limit: int = yaml_data["parameters"]["max_token_limit"]

    def transform(self, args: TextChunkerInputDict) -> TextChunkerOutputDict:
        if self.tokenization_library == "nltk":
            nltk.download("punkt")
            sentences = nltk.sent_tokenize(args.cleaned_text)
        elif self.tokenization_library == "spacy":
            nlp = spacy.load("en_core_web_sm")
            doc = nlp(args.cleaned_text)
            sentences = [sent.text for sent in doc.sents]
        else:
            raise ValueError("Invalid tokenization_library provided. Must be 'nltk' or 'spacy'.")

        text_chunks = []
        current_chunk = ""

        for sentence in sentences:
            if len(current_chunk + sentence) < self.max_token_limit:
                current_chunk += sentence
            else:
                text_chunks.append(current_chunk.strip())
                current_chunk = sentence

        if current_chunk.strip():
            text_chunks.append(current_chunk.strip())

        return TextChunkerOutputDict(text_chunks=text_chunks)

load_dotenv()
text_chunker_app = FastAPI()

@text_chunker_app.post("/transform/")
async def transform(args: TextChunkerInputDict) -> TextChunkerOutputDict:
    text_chunker = TextChunker()
    return text_chunker.transform(args)
