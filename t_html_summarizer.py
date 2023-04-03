
import pytest
from fastapi.testclient import TestClient
from typing import Tuple
from pydantic import ValidationError
from your_module import HtmlSummarizer, HtmlSummarizerIn, HtmlSummarizerOut

test_data = [
    (
        "https://example.com/article1",
        "This is a summary of article 1 from example.com.",
    ),
    (
        "https://example.com/article2",
        "This is a summary of article 2 from example.com.",
    ),
    (
        "https://example.com/article3",
        "This is a summary of article 3 from example.com.",
    ),
]

invalid_test_data = [
    "",
    "not-a-url",
]


@pytest.mark.parametrize("url,expected_summary", test_data)
async def test_html_summarizer_transform(url: str, expected_summary: str):
    html_summarizer = HtmlSummarizer()
    input_data = HtmlSummarizerIn(url=url)
    output_data = await html_summarizer.transform(input_data, callbacks=None)
    assert output_data.summary == expected_summary


@pytest.mark.parametrize("invalid_url", invalid_test_data)
async def test_html_summarizer_transform_on_invalid_url(invalid_url: str):
    with pytest.raises(ValidationError):
        HtmlSummarizerIn(url=invalid_url)
