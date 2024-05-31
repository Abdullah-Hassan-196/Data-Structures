class PerfectHash:
    def __init__(self, keys):
        self.keys = keys
        self.hash_table = {}

    def build(self):
        for i, key in enumerate(self.keys):
            self.hash_table[key] = i

    def contains(self, key):
        return key in self.hash_table

def main():
    # Example keys
    keys = [10, 25, 42, 17, 33, 50]

    # Create a perfect hash data structure
    perfect_hash = PerfectHash(keys)

    # Build the perfect hash
    perfect_hash.build()

    # Check if a key exists
    key_to_check = 42
    if perfect_hash.contains(key_to_check):
        print(f"The key {key_to_check} exists in the perfect hash.")
    else:
        print(f"The key {key_to_check} does not exist in the perfect hash.")

    # Check another key
    key_to_check = 99
    if perfect_hash.contains(key_to_check):
        print(f"The key {key_to_check} exists in the perfect hash.")
    else:
        print(f"The key {key_to_check} does not exist in the perfect hash.")

if __name__ == "__main__":
    main()
