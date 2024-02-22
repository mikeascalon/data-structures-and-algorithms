from data_structures.hashtable import Hashtable


def left_join(hashmap1, hashmap2):
    """
    Perform a left join between two hash maps.
    
    Args:
    - hashmap1: Hash map with word strings as keys and their synonyms as values.
    - hashmap2: Hash map with word strings as keys and their antonyms as values.
    
    Returns:
    - A list of tuples, where each tuple contains:
        - The key from hashmap1.
        - The synonym from hashmap1.
        - The antonym from hashmap2 if the key exists in hashmap2, otherwise None.
    """
    result = []
    for key in hashmap1:
        synonym = hashmap1[key]
        antonym = hashmap2.get(key, "NONE")  # Use "NONE" for missing antonyms
        result.append([key, synonym, antonym])
    return result