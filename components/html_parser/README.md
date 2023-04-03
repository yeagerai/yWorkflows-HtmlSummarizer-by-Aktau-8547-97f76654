markdown
# Component Name
HtmlParser

# Description
The HtmlParser component is a Yeager component designed to parse and extract selected text from the provided HTML content. This component is implemented as a Python class named `HtmlParser`, which inherits from the `AbstractComponent` base class.

# Input and Output Models
The HtmlParser component uses two Pydantic-based models for validating, serializing, and deserializing input and output data.

## Input Model:
- **HtmlParserInputDict**: A single field model that holds the input data for the component.
    - `html_content` (str): The HTML content to be parsed.

## Output Model:
- **HtmlParserOutputDict**: A single field model that holds the output data for the component.
    - `parsed_text` (str): The extracted text from the HTML content.

# Parameters
The HtmlParser component has one user-defined parameter:

- `tags_to_extract` (List[str]): A list of HTML tags to be extracted from the HTML content. This parameter is loaded from the component configuration file (YAML) at initialization.

# Transform Function
The `transform()` method of the HtmlParser component performs the following steps:

1. Create a BeautifulSoup object named `soup` from the input `html_content`, using the `html.parser` parser.
2. Initialize an empty string named `parsed_text` to store the extracted text.
3. Iterate over each tag in the `tags_to_extract` list:
   - Find all elements with the given tag using `soup.find_all(tag)`.
   - Iterate over each element found and append the text content of the element to the `parsed_text` string, followed by a newline character.
4. Return an instance of `HtmlParserOutputDict` with the `parsed_text` field set to the final extracted text.

# External Dependencies
The HtmlParser component uses the following external libraries:

- `bs4` (Beautiful Soup 4): Used to parse the input HTML content and extract text from the specified tags.
- `pydantic`: Used for creating and validating input and output models.
- `fastapi`: Used to create an API endpoint for the `HtmlParser.transform()` method.

# API Calls
The HtmlParser component does not make any external API calls.

# Error Handling
Beautiful Soup handles parsing errors internally and attempts to repair any improperly formatted HTML. No specific exception handling is needed within the `transform()` method.

# Examples
To use the HtmlParser component within a Yeager Workflow, create an instance of the HtmlParser class, and call the `transform()` method with the input data encapsulated in an `HtmlParserInputDict`.

