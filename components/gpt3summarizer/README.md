markdown
# Component Name
Gpt3Summarizer

# Description
The Gpt3Summarizer is a Yeager component designed to summarize text passed through Yeager Workflows using the OpenAI GPT-3 API. It takes a list of text chunks as input, summarizes each chunk using GPT-3, and returns a list of corresponding summaries as output.

# Input and Output Models
- *Input Model:* Gpt3SummarizerInputDict
  - **text_chunks:** List[str] - A list of text string chunks to be summarized.

- *Output Model:* Gpt3SummarizerOutputDict
  - **summaries:** List[str] - A list of summarized text strings corresponding to the input text chunks.

Both input and output models inherit from BaseModel provided by the Pydantic library, ensuring correct validation and serialization of data.

# Parameters
- *api_key:* Optional[str] - The API key used for authentication with the OpenAI GPT-3 API. Obtained from environment variables.
- *engine:* str - The OpenAI engine to be used for text summarization (e.g., "davinci-codex").
- *temperature:* float - Temperature for the GPT-3 API request, controlling the creativity of the generated summary.
- *max_tokens:* int - Maximum number of tokens allowed in the generated summary.

# Transform Function
The transform() method processes input data in the following steps:
1. Set the GPT-3 API key from the component's api_key attribute.
2. Initialize an empty list to store generated summaries.
3. Iterate over the input text_chunks list.
   a. For each chunk, create an OpenAI API completion request with the specified engine, prompt, temperature, and max_tokens parameters.
   b. Extract the generated summary from the API response.
   c. Append the summary to the summaries list after removing any leading or trailing whitespace.
4. Return the Gpt3SummarizerOutputDict object containing the generated summaries list.

# External Dependencies
- *os*: Manage environment variables.
- *yaml*: Parse component configuration files.
- *dotenv*: Load environment variables from a `.env` file.
- *FastAPI*: Create and manage the FastAPI web application.
- *pydantic*: Define input and output models for data validation and serialization.
- *openai*: Interact with OpenAI GPT-3 API.

# API Calls
The component uses the [OpenAI GPT-3 API](https://beta.openai.com/docs/) to generate text summaries. Specifically, it makes `Completion.create` requests with the provided engine, temperature, and max_tokens parameters. API calls are made for each chunk of input text during the transform() method execution.

# Error Handling
Errors are handled using the built-in error handling mechanisms provided by the FastAPI and Pydantic libraries. These libraries will automatically validate input and output data, and raise appropriate exceptions in case of data inconsistencies or failed API calls.

# Examples
To use the Gpt3Summarizer component within a Yeager Workflow, follow these steps:
1. Set up the appropriate environment variables in a `.env` file, such as the OpenAI API key:
   