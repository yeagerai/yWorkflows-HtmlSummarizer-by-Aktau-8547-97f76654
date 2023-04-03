
# TextCleaner

Processes the extracted text from an HtmlParser component to remove extra whitespace, line breaks, special characters, and HTML entities. Outputs the cleaned text as a single string.

## Initial generation prompt
description: Processes the extracted text to remove extra whitespace, line breaks,
  special characters, and HTML entities, and outputs the cleaned text.
input_from: HtmlParser
name: TextCleaner


## Transformer breakdown
- 1. Remove line breaks and extra whitespace from the input raw_text.
- 2. If remove_html_entities is True, remove HTML entities from the text.
- 3. If remove_special_characters is True, remove special characters from the text.
- 4. Return the processed cleaned_text.

## Parameters
[{'name': 'remove_html_entities', 'default_value': 'True', 'description': 'Toggle whether to remove HTML entities from the text.', 'type': 'bool'}, {'name': 'remove_special_characters', 'default_value': 'True', 'description': 'Toggle whether to remove special characters from the text.', 'type': 'bool'}]

        