from data_structures.linked_list import LinkedList

class Hashtable:
    """
    A Hashtable implementation that uses separate chaining for collision resolution.
    The hashtable is backed by a fixed-size array of linked lists (buckets), where each
    list stores key-value pairs (drops) that hash to the same bucket index.

    Attributes:
        _size (int): The number of buckets in the hashtable. Default is 1024.
        _buckets (list of LinkedList or None): The array of buckets. Each bucket is
            either None or a LinkedList containing key-value pairs.

    Methods:
        __init__(self, size=1024): Initializes the hashtable with a specific size.
        set(self, key, value): Inserts or updates a key-value pair in the hashtable.
        get(self, key): Retrieves the value associated with the given key.

    Usage:
        hashtable = Hashtable(size=1024)  # Create a new hashtable
        hashtable.set('key1', 'value1')   # Insert a key-value pair
        value = hashtable.get('key1')     # Retrieve the value for 'key1'
    """

    def __init__(self, size=1024):
        """
        Initializes the hashtable with a specific size.

        Parameters:
            size (int): The size of the hashtable (number of buckets). Default is 1024.
        """
        self._size = size
        self._buckets = [None] * size

    def set(self, key, value):
        """
        Inserts or updates a key-value pair in the hashtable. If the key already exists,
        its value is updated. Otherwise, the key-value pair is inserted.

        Parameters:
            key: The key of the key-value pair. Should be hashable.
            value: The value associated with the key.
        """
        index = self._hash(key)
        bucket = self._buckets[index]
        if bucket is None:
            bucket = LinkedList()
            self._buckets[index] = bucket

        current = bucket.head

        while current:
            candidate_drop = current.value
            if candidate_drop[0] == key:
                # Found preexisting key, update the value
                candidate_drop[1] = value
                return

        # No preexisting key found, add new key-value pair
        drop = [key, value]
        bucket.insert(drop)

    def get(self, key):
        """
        Retrieves the value associated with the given key in the hashtable. If the key
        does not exist, None is returned.

        Parameters:
            key: The key whose value is to be retrieved.

        Returns:
            The value associated with the key, or None if the key does not exist.
        """
        index = self._hash(key)
        bucket = self._buckets[index]

        if bucket is None:
            return None

        current = bucket.head

        while current:
            drop = current.value  # key-value pair
            if drop[0] == key:
                return drop[1]

            current = current.next

        return None

    def _hash(self, key):
        """
        Hashes the given key into an index for the buckets array.

        Parameters:
            key: The key to hash.

        Returns:
            An index in the range [0, self._size).
        """
        # Implement the hash function here (example placeholder)
        return hash(key) % self._size


    def has(self, key):
        """
        Checks if the specified key exists in the hashtable.

        Parameters:
            key: The key to check in the hashtable.

        Returns:
            Boolean indicating whether the key exists.
        """
        index = self._hash(key)
        bucket = self._buckets[index]
        if bucket is None:
            return False

        current = bucket.head
        while current:
            if current.value[0] == key:
                return True
            current = current.next
        return False

    def keys(self):
        """
        Returns a collection of all keys stored in the hashtable.

        Returns:
                A list containing all unique keys in the hashtable.
        """
        keys_list = []
        for bucket in self._buckets:
            if bucket is not None:
                current = bucket.head
                while current:
                    keys_list.append(current.value[0])
                    current = current.next
        return keys_list
