class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash_function(key)
        self.table[index].append((key, value))

    def search(self, key):
        index = self._hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def delete(self, key):
        index = self._hash_function(key)
        for i, (k, _) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return True
        return False

def main():
    # Create a hash table with size 10
    hash_table = HashTable(10)

    # Insert key-value pairs
    hash_table.insert("apple", 5)
    hash_table.insert("banana", 7)
    hash_table.insert("orange", 3)

    # Search for values
    print("Value for 'apple':", hash_table.search("apple"))
    print("Value for 'banana':", hash_table.search("banana"))
    print("Value for 'orange':", hash_table.search("orange"))

    # Delete a key
    hash_table.delete("banana")

    # Search again after deletion
    print("Value for 'banana' after deletion:", hash_table.search("banana"))  # Should print None

main()
