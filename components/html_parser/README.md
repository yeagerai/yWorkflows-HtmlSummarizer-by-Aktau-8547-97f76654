
# HtmlParser

Uses Beautiful Soup library to parse the HTML content obtained from HtmlReader, extracting the relevant text within HTML tags and storing the text data. This component processes the raw HTML content and simplifies it by removing unnecessary tags and elements, resulting in a more structured and readable format.

## Initial generation prompt
description: Uses Beautiful Soup library to parse the HTML content obtained from HtmlReader,
  extracting the relevant text within HTML tags and storing the text data.
input_from: HtmlReader
name: HtmlParser


## Transformer breakdown
- 1. Initialize a Beautiful Soup object with the input html_content.
- 2. For each tag in the tags_to_extract list, find all occurrences within the HTML.
- 3. Extract the text within each found tag and combine them to form the parsed_text.
- 4. Return the parsed_text as output.

## Parameters
[{'name': 'tags_to_extract', 'default_value': ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'], 'description': 'A list of HTML tags (strings) to be extracted from the input HTML content.', 'type': 'list'}]

        