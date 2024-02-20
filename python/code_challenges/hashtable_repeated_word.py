from data_structures.hashtable import Hashtable
import re


def first_repeated_word(input_string):
    if not input_string.strip():
        # If the string is empty or only contains whitespace, return None
        return None
    
    # Convert the string to lowercase to make the search case-insensitive
    input_string = input_string.lower()

    # Split the input string on spaces to get words with punctuation
    words_with_punct = input_string.split()

    # Initialize an empty set to keep track of seen words
    seen_words = set()

    # Process each word in the list
    for word in words_with_punct:
        # Remove a single punctuation mark from the end of the word, if present
        word = re.sub(r'[,.!?;:"]$', '', word)

        # Check if the word is in the set of seen words
        if word in seen_words:
            return word
        # Add the word to the set of seen words
        seen_words.add(word)
    
    # If no word is repeated, return None
    return None