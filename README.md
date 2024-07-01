# Word Match Script

This script reads a list of predefined words from a file and matches them against words in an input text file. The matched words are then printed to the console.

## Requirements

- Python 3.x
- Logging module (part of the Python standard library)

## How to Use

1. **Prepare the predefined words file:**
    - Create a file named `predefined_words.txt`.
    - Add one word per line. For example:

        ```
        apple
        banana
        cherry
        ```

2. **Prepare the input text file:**
    - Create a file named `input_file.txt`.
    - Add the text you want to search through. For example:

        ```
        I have an apple and a banana.
        Do you have a cherry?
        ```

3. **Run the script:**
    - Ensure the script and the two text files are in the same directory.
    - Run the script from the command line:

        ```
        python word_match.py
        ```

## Code Overview

### `load_predefined_words(predefined_text_file)`

- Reads the predefined words from the specified file.
- Returns a set of predefined words.
- Logs the number of words loaded.
- Handles `FileNotFoundError` and other exceptions, logging appropriate error messages.

### `word_match(input_text_file, predefined_words)`

- Reads the input text file and finds matches with the predefined words.
- Returns a set of matched words.
- Logs the number of matches found.
- Handles `FileNotFoundError` and other exceptions, logging appropriate error messages.

### `main(predefined_text_file, input_text_file)`

- Loads predefined words using `load_predefined_words()`.
- If no predefined words are loaded, logs a warning and exits.
- Finds matches using `word_match()`.
- Returns the matched words.

### Execution

- The script defines the paths to `predefined_words.txt` and `input_file.txt`.
- The `main` function is called if the script is run directly.
- Matched words are printed to the console and logged.

## Example Output

    ```
    2023-07-01 12:34:56,789 - INFO - Loaded 3 predefined words from predefined_words.txt.
    2023-07-01 12:34:56,790 - INFO - Found 2 matches in input_file.txt.
    Matched Words:
    apple
    banana
    cherry
    ```

## Error Handling

- If `predefined_words.txt` or `input_file.txt` is not found, an error message is logged.
- Other exceptions are caught and logged with an appropriate error message.

## Logging

- The script logs events at different levels (INFO, WARNING, ERROR) to provide detailed information about its execution.
- Logs include timestamps for easier tracking of events.

## Assumptions

- The predefined words file (`predefined_words.txt`) contains one word per line.
- The input text file (`input_file.txt`) contains plain text with words separated by whitespace or punctuation.
- Both files are located in the same directory as the script.
- The script is run in an environment where Python 3 is installed.
- Words are compared in a case-insensitive manner (e.g., "Cherry" and "cherry" are considered the same).
- Plural forms (e.g., "cherries" and "cherry") are considered different words.


