
import pytest
from pydantic import ValidationError
from typing import List
from core.text_chunker import TextChunker, TextChunkerInputDict, TextChunkerOutputDict


@pytest.mark.parametrize(
    "input_data, expected_output_data",
    [
        (
            TextChunkerInputDict(cleaned_text="This is a test. Let's see how it works."),
            TextChunkerOutputDict(text_chunks=["This is a test.", "Let's see how it works."]),
        ),
        (
            TextChunkerInputDict(cleaned_text=""),
            TextChunkerOutputDict(text_chunks=[]),
        ),
        (
            TextChunkerInputDict(cleaned_text="One sentence."),
            TextChunkerOutputDict(text_chunks=["One sentence."]),
        ),
        (
            TextChunkerInputDict(cleaned_text="A very long sentence that spans for more than the max_token_limit causing it to be split into multiple chunks."),
            TextChunkerOutputDict(text_chunks=["A very long sentence", "that spans for more than the", "max_token_limit causing it", "to be split into multiple", "chunks."]),
        ),
    ],
)
def test_text_chunker_transform(input_data: TextChunkerInputDict, expected_output_data: TextChunkerOutputDict):
    text_chunker = TextChunker()
    output_data = text_chunker.transform(input_data)
    assert output_data == expected_output_data


@pytest.mark.parametrize(
    "invalid_input_data",
    [
        {"invalid_key": "Some invalid data"},
        {"cleaned_text": 123},
    ],
)
def test_text_chunker_transform_validation_error(invalid_input_data):
    with pytest.raises(ValidationError):
        TextChunkerInputDict(**invalid_input_data)


def test_text_chunker_invalid_tokenization_library():
    text_chunker = TextChunker()
    text_chunker.tokenization_library = "invalid_lib"
    input_data = TextChunkerInputDict(cleaned_text="This is a test. Let's see how it works.")

    with pytest.raises(ValueError, match="Invalid tokenization_library provided. Must be 'nltk' or 'spacy'."):
        text_chunker.transform(input_data)
