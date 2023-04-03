markdown
# Component Name
TextCleaner

# Description
The TextCleaner component is a building block within a Yeager Workflow, designed to process and clean raw text inputs by removing unnecessary spaces, HTML entities, and special characters, depending on the parameters set for the component.

# Input and Output Models
The TextCleaner component uses Pydantic models to define and validate the input and output data types.

**Input Model:**
* `TextCleanerInputDict`: A BaseModel containing a single field `raw_text` (str) which represents the input text to be cleaned.

**Output Model:**
* `TextCleanerOutputDict`: A BaseModel containing a single field `cleaned_text` (str) which represents the processed and cleaned text after applying the TextCleaner transform() method.

# Parameters
The component uses the following parameters, loaded from a configuration file:

* `remove_html_entities` (bool): Determines if the component should remove HTML entities from the input text. Default value is determined by the configuration file.
* `remove_special_characters` (bool): Determines if the component should remove special characters from the input text. Default value is determined by the configuration file.

# Transform Function
The `transform()` method of the TextCleaner component processes the input data according to the following steps:

1. Remove unnecessary spaces from the input text using the split() and join() methods.
2. If the `remove_html_entities` parameter is True, remove HTML entities from the text using the `html.unescape()` method.
3. If the `remove_special_characters` parameter is True, remove special characters from the text using a regex pattern and the `re.sub()` method.
4. Return the cleaned text as part of the `TextCleanerOutputDict` object.

# External Dependencies
The TextCleaner component relies on the following external libraries:

* `html`: Standard Python library for working with HTML entities.
* `re`: Standard Python library for working with regular expressions
* `pydantic`: A library for data validation and parsing.
* `fastapi`: A lightweight web framework for creating APIs.
* `yaml`: Library for working with YAML data.
* `dotenv`: A library for loading environment variables from `.env` files.

# API Calls
The component does not make any external API calls.

# Error Handling
The TextCleaner component relies on the error handling mechanisms provided by the FastAPI and Pydantic libraries. Input data that fails the Pydantic validation will result in an error response with a clear message detailing the validation error(s).

# Examples
To use the TextCleaner component within a Yeager Workflow:

1. Configure the necessary parameters in the component's configuration file as desired (e.g., whether to remove HTML entities, special characters, or both).
2. Create an instance of the TextCleaner class and call its transform() method with a valid `TextCleanerInputDict` object containing the raw text to be cleaned.
3. The transform() method will return a `TextCleanerOutputDict` object containing the cleaned text.
