
# TextChunker

The TextChunker component splits the cleaned text into smaller chunks using sentence tokenization with NLTK or spaCy, ensuring that the chunks are compatible with GPT-3's maximum token limit. This allows for efficient processing of large input texts by conforming to the constraints of the GPT-3 API while preserving sentence structure and meaning.

## Initial generation prompt
description: Splits the cleaned text into smaller chunks using sentence tokenization
  with NLTK or spaCy, ensuring that the chunks are compatible with GPT-3's maximum
  token limit.
input_from: TextCleaner
name: TextChunker


## Transformer breakdown
- 1. Import the chosen tokenization library (NLTK or spaCy)
- 2. Perform sentence tokenization on cleaned_text
- 3. Iterate through sentences and group them into text_chunks
- 4. Ensure each text_chunk does not exceed max_token_limit
- 5. Return text_chunks

## Parameters
[{'name': 'tokenization_library', 'default_value': 'nltk', 'description': "The library to be used for sentence tokenization, either 'nltk' or 'spacy'", 'type': 'string'}, {'name': 'max_token_limit', 'default_value': 2048, 'description': 'The maximum number of tokens allowed in a single text chunk for GPT-3', 'type': 'int'}]

        