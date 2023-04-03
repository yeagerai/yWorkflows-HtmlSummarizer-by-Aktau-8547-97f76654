
import pytest
from typing import List
from pydantic import BaseModel
from .your_component_directory import SummaryConcatenator, Gpt3SummarizerOutput, HtmlSummarizerOutputModel

# Mocked input data
input_data = [
    ([Gpt3SummarizerOutput(summary="Summary 1."), Gpt3SummarizerOutput(summary="Summary 2.")], HtmlSummarizerOutputModel(concatenated_summary="Summary 1.Summary 2.")),
    ([Gpt3SummarizerOutput(summary="Summary A."), Gpt3SummarizerOutput(summary="Summary B.")], HtmlSummarizerOutputModel(concatenated_summary="Summary A.Summary B.")),
    ([], HtmlSummarizerOutputModel(concatenated_summary="")),
]

# Test cases
@pytest.mark.parametrize("input_list, expected_output", input_data)
def test_summary_concatenator(input_list: List[Gpt3SummarizerOutput], expected_output: HtmlSummarizerOutputModel):
    # Initialize the SummaryConcatenator component
    summary_concat = SummaryConcatenator()

    # Call the transform method with the mocked input data
    output = summary_concat.transform(input_list)

    # Assert that the output matches the expected output
    assert output == expected_output
