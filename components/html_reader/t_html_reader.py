
import pytest
import requests_mock
from fastapi.testclient import TestClient
from core.abstract_component import AbstractComponent
from .html_reader import (
    HtmlReader,
    HtmlReaderInputDict,
    HtmlReaderOutputDict,
    html_reader_app,
)

client = TestClient(html_reader_app)

test_cases = [
    (
        "https://example.com",
        "<html><head><title>Example</title></head><body><h1>Example Website</h1></body></html>",
    ),
    (
        "https://test.com",
        "<html><head><title>Test</title></head><body><h1>Test Website</h1></body></html>",
    ),
]

@pytest.mark.parametrize("url, expected_html", test_cases)
def test_html_reader_transform(url: str, expected_html: str):
    # Arrange
    input_data = HtmlReaderInputDict(url=url)
    expected_output = HtmlReaderOutputDict(html_content=expected_html)

    with requests_mock.Mocker() as m:
        m.get(url, text=expected_html)

        # Act
        response = client.post("/transform/", json=input_data.dict())

        # Assert
        assert response.status_code == 200
        assert response.json() == expected_output.dict()

@pytest.mark.parametrize("url", ["", "not a url"])
def test_html_reader_transform_invalid_input(url: str):
    # Arrange
    input_data = HtmlReaderInputDict(url=url)
    
    # Act
    response = client.post("/transform/", json=input_data.dict())

    # Assert
    assert response.status_code == 422
