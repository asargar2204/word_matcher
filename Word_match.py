import re
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_predefined_words(predefined_text_file):
    try:
        with open(predefined_text_file, 'r') as file:
            words = set(word.strip().lower() for word in file)
        logging.info(f"Loaded {len(words)} predefined words from {predefined_text_file}.")
        return words
    except FileNotFoundError:
        logging.error(f"File {predefined_text_file} not found.")
        return set()
    except Exception as e:
        logging.error(f"An error occurred while loading predefined words: {e}")
        return set()

def word_match(input_text_file, predefined_words):
    match = set()
    word_pattern = re.compile(r'\b\w+\b')
    try:
        with open(input_text_file, 'r') as inputFile:
            for line in inputFile:
                words = word_pattern.findall(line.lower())
                match.update(word for word in words if word in predefined_words)
        logging.info(f"Found {len(match)} matches in {input_text_file}.")
    except FileNotFoundError:
        logging.error(f"File {input_text_file} not found.")
    except Exception as e:
        logging.error(f"An error occurred while matching words: {e}")
    
    return match

def main(predefined_text_file, input_text_file):
    predefined_words = load_predefined_words(predefined_text_file)
    if not predefined_words:
        logging.warning("No predefined words loaded. Exiting.")
        return set()
    matches = word_match(input_text_file, predefined_words)
    return matches

predefined_text_file = 'predefined_words.txt'
input_text_file = 'input_file.txt'

if __name__ == "__main__":
    matches = main(predefined_text_file, input_text_file)
    if matches:
        logging.info("Matched Words:")
        for match in matches:
            print(match)
    else:
        logging.info("No matches found.")
