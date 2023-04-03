
# Gpt3Summarizer

Uses OpenAI's GPT-3 API to generate summaries for each text chunk. Each chunk is processed with the appropriate GPT-3 API call (davinci, curie, babbage, or ada) and a summary is returned.

## Initial generation prompt
description: Uses OpenAI's GPT-3 API to generate summaries for each text chunk. Each
  chunk is processed with the appropriate GPT-3 API call (davinci, curie, babbage,
  or ada) and a summary is returned.
input_from: TextChunker
name: Gpt3Summarizer


## Transformer breakdown
- 1. Iterate through the input text_chunks.
- 2. For each chunk:
- 2.1. Call the appropriate GPT-3.5 turbo API endpoint.
- 2.2. Extract the generated summary from the API response.
- 2.3. Add the summary to the list of summaries.
- 3. Return the list of summaries.

## Parameters
[{'name': 'api_key', 'description': "OpenAI's GPT-3 API key.", 'type': 'str', 'default_value': None}, {'name': 'engine', 'description': 'The GPT-3 engine to use for summarization (davinci, curie, babbage, or ada).', 'type': 'str', 'default_value': 'curie'}, {'name': 'temperature', 'description': 'The sampling temperature to control the randomness of the summaries.', 'type': 'float', 'default_value': 0.7}, {'name': 'max_tokens', 'description': 'The maximum number of tokens allowed in the generated summaries.', 'type': 'int', 'default_value': 150}]

        