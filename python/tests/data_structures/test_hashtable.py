import pytest
from data_structures.hashtable import Hashtable


def test_exists():
    assert Hashtable


# @pytest.mark.skip("TODO")
def test_get_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_set_and_get_value():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    assert hashtable.get("apple") == "Used for apple sauce", "Setting a key/value should result in the value being in the data structure."

# @pytest.mark.skip("TODO")
def test_get_nonexistent_key_returns_none():
    hashtable = Hashtable()
    assert hashtable.get("banana") is None, "Retrieving a non-existent key should return None."

# @pytest.mark.skip("TODO")
def test_get_all_unique_keys():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    hashtable.set("banana", "Used for banana bread")
    keys = hashtable.keys()
    assert set(keys) == {"apple", "banana"}, "Should return a list of all unique keys."

# @pytest.mark.skip("TODO")
def test_handle_collision_and_retrieve_value():
    hashtable = Hashtable(1)  # Small size to force a collision
    hashtable.set("apple", "Used for apple sauce")
    hashtable.set("elppa", "Used for apple pie")  # Assuming simple hash function that could result in collision
    assert hashtable.get("apple") == "Used for apple sauce", "Should handle a collision within the hashtable."
    assert hashtable.get("elppa") == "Used for apple pie", "Should retrieve a value from a bucket within the hashtable that has a collision."

# @pytest.mark.skip("TODO")
def test_hash_in_range():
    hashtable = Hashtable(1024)
    index = hashtable._hash("apple")  # Accessing the protected hash method directly for testing
    assert 0 <= index < 1024, "Hashed key index should be within range."


# @pytest.mark.skip("TODO")
def test_key_exists():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    assert hashtable.has("apple") == True, "Should return True if a key exists."
    assert hashtable.has("banana") == False, "Should return False if a key does not exist."


def test_collision_handling():
    hashtable = Hashtable(1)  # Force collisions by using a small hashtable size
    hashtable.set("apple", "Used for apple sauce")
    hashtable.set("banana", "Used for banana bread")
    assert hashtable.get("apple") == "Used for apple sauce", "Should successfully handle collisions."
    assert hashtable.get("banana") == "Used for banana bread", "Should retrieve correct value despite collisions."

# @pytest.mark.skip("TODO")
def test_internals():
    hashtable = Hashtable(1024)
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")

    actual = []

    # NOTE: purposely breaking encapsulation to test the "internals" of Hashmap
    for item in hashtable._buckets:
        if item:
            actual.append(item.display())

    expected = [[["silent", True], ["listen", "to me"]], [["ahmad", 30]]]

    assert actual == expected
