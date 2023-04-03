
import os
import pytest
from pydantic import ValidationError
from typing import Tuple
from bs4 import BeautifulSoup
from core.abstract_component import AbstractComponent
from my_project.components.html_parser import (
    HtmlParser,
    HtmlParserInputDict,
    HtmlParserOutputDict,
)

test_data = [
    (
        "<div>Hello World!</div><p>This is an example</p>",
        ["div", "p"],
        "Hello World!\nThis is an example\n",
    ),
    (
        "<div><p>Nested elements</p></div>",
        ["div"],
        "<p>Nested elements</p>\n",
    ),
    (
        "<h1>Headline 1</h1><h2>Headline 2</h2>",
        ["h1"],
        "Headline 1\n",
    ),
    (
        "",
        ["div"],
        "",
    ),
]

@pytest.mark.parametrize("html_content, tags_to_extract, expected_output", test_data)
def test_html_parser(
    html_content: str,
    tags_to_extract: Tuple[str],
    expected_output: str,
    monkeypatch,
) -> None:
    # Mock the tags_to_extract from configuration file
    def mock_load_tags_to_extract(*args, **kwargs):
        return {"parameters": {"tags_to_extract": list(tags_to_extract)}}

    monkeypatch.setattr(AbstractComponent, "load_parameters", mock_load_tags_to_extract)

    # Create an HtmlParser instance
    html_parser = HtmlParser()

    # Call the transform method with the mocked input data
    input_data = HtmlParserInputDict(html_content=html_content)
    output_data = html_parser.transform(input_data)

    # Assert that the output matches the expected_output
    assert output_data.parsed_text == expected_output

    if not html_content:
        with pytest.raises(ValidationError):
            HtmlParserInputDict(html_content=None)

def test_edge_cases():
    # Test for invalid tags if necessary
    pass
