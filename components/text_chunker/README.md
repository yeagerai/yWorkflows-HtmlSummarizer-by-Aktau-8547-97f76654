markdown
# Component Name
TextChunker

# Description
TextChunker is a Yeager component designed to split a given text into smaller chunks without exceeding a specified token limit. The component uses tokenization libraries like NLTK and spaCy to divide the input text into sentences before further breaking it into chunks based on the token limit.

# Input and Output Models
## Input Model: `TextChunkerInputDict`
- **cleaned_text** (str): The input text to be chunked.

## Output Model: `TextChunkerOutputDict`
- **text_chunks** (List[str]): A list of text chunks generated after splitting the input text.

# Parameters
- **tokenization_library** (str): The tokenization library to be used for splitting the input text into sentences. Supported values are 'nltk' or 'spacy'.
- **max_token_limit** (int): The maximum token limit for each text chunk. No text chunk should exceed this token limit.

# Transform Function
The `transform()` method is responsible for implementing the text chunking based on the specified input and component parameters. It performs the following steps:
1. Based on the selected tokenization_library, it splits the input text into sentences using either the NLTK library's `sent_tokenize()` method or spaCy's `nlp()` method and sentence tokenization.
2. Initializes an empty list called `text_chunks` to store the chunks and a string `current_chunk` to store the current text chunk being processed.
3. Iterates through the sentences, and for each sentence, checks if appending the sentence to the `current_chunk` would result in exceeding the `max_token_limit`.
4. If the limit is not exceeded, the sentence is appended to the `current_chunk`. Otherwise, the current chunk is added to the `text_chunks` list, and the current sentence becomes the new `current_chunk`.
5. If there are any remaining sentences in the `current_chunk` after processing all the sentences, the final `current_chunk` is added to the `text_chunks` list.
6. Returns the `TextChunkerOutputDict`, containing the generated text chunks.

# External Dependencies
- **os:** Used for handling environment variables.
- **typing:** Provides the List typing for defining the input and output models.
- **fastapi:** Provides the FastAPI class to create the API for the component.
- **pydantic:** Provides the BaseModel for defining the input and output models.
- **yaml:** Used for parsing and loading the component's configuration file.
- **nltk:** Provides the tokenization functions when using the NLTK library for tokenization.
- **spacy:** Provides the tokenization functions when using the spaCy library for tokenization.

# API Calls
This component does not make any external API calls.

# Error Handling
The component raises a `ValueError` if an invalid value for the `tokenization_library` parameter is provided. The error message states that the library value must be either 'nltk' or 'spacy'.

# Examples
Below is an example of how to use TextChunker in a Yeager Workflow:

1. Configure the `config.yaml` file for the TextChunker component:

