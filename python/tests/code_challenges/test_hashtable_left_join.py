import pytest
from code_challenges.hashtable_left_join import left_join


def test_exists():
    assert left_join


# @pytest.mark.skip("TODO")
def test_example():
    synonyms = {
        "diligent": "employed",
        "fond": "enamored",
        "guide": "usher",
        "outfit": "garb",
        "wrath": "anger",
    }
    antonyms = {
        "diligent": "idle",
        "fond": "averse",
        "guide": "follow",
        "flow": "jam",
        "wrath": "delight",
    }

    expected = [
        ["diligent", "employed", "idle"],
        ["fond", "enamored", "averse"],
        ["guide", "usher", "follow"],
        ["outfit", "garb", "NONE"],
        ["wrath", "anger", "delight"],
        
    ]

    actual = left_join(synonyms, antonyms)

    assert actual == expected

def test_no_matching_keys():
    synonyms = {"happy": "joyful", "bright": "luminous"}
    antonyms = {"sad": "unhappy", "dark": "dim"}
    expected = [
        ["happy", "joyful", "NONE"],
        ["bright", "luminous", "NONE"],
    ]
    actual = left_join(synonyms, antonyms)
    assert actual == expected

def test_empty_dictionaries():
    synonyms = {}
    antonyms = {}
    expected = []
    actual = left_join(synonyms, antonyms)
    assert actual == expected

def test_all_keys_have_antonyms():
    synonyms = {
        "large": "big",
        "small": "tiny",
        "cold": "chilly",
        "hot": "warm",
    }
    antonyms = {
        "large": "small",
        "small": "large",
        "cold": "hot",
        "hot": "cold",
    }
    expected = [
        ["large", "big", "small"],
        ["small", "tiny", "large"],
        ["cold", "chilly", "hot"],
        ["hot", "warm", "cold"],
    ]
    actual = left_join(synonyms, antonyms)
    assert actual == expected