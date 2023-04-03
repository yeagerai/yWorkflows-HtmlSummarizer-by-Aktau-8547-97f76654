
import pytest
from pydantic import ValidationError
from components.text_cleaner import TextCleaner, TextCleanerInputDict, TextCleanerOutputDict


# Define test cases with mocked input and expected output data
test_cases = [
    ("Sample text with <b>HTML tags</b> & special_chars!", True, True, "Sample text with HTML tags special chars"),
    ("Sample text without HTML tags but with special characters: @#$%", True, True, "Sample text without HTML tags but with special characters"),
    ("Sample text with <b>HTML tags</b> & without special_chars!", True, False, "Sample text with HTML tags & without special_chars!"),
    ("Sample text without HTML tags or special characters", False, False, "Sample text without HTML tags or special characters"),
]

# Use @pytest.mark.parametrize to create multiple test scenarios
@pytest.mark.parametrize("input_text,remove_html_entities,remove_special_characters,expected_output", test_cases)
def test_text_cleaner_transform(input_text: str, remove_html_entities: bool, remove_special_characters: bool, expected_output: str):
    # Create a TextCleaner instance with the desired configuration
    text_cleaner = TextCleaner()
    text_cleaner.remove_html_entities = remove_html_entities
    text_cleaner.remove_special_characters = remove_special_characters

    # Create a TextCleanerInputDict with the mocked input data
    input_data = TextCleanerInputDict(raw_text=input_text)

    # Call the transform() method and assert the output matches the expected output
    output_data = text_cleaner.transform(input_data)
    assert output_data.cleaned_text == expected_output


# Test input validation with an invalid data type
def test_transform_input_validation():
    with pytest.raises(ValidationError):
        TextCleanerInputDict(raw_text=123)  # Expect an error because the raw_text should be a string


# Add any additional edge case scenarios or error handling tests as necessary
