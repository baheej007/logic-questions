class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def set(self, key, value):
        idx = self._hash(key)
        self.table[idx] = (key, value)

    def get(self, key):
        idx = self._hash(key)
        if self.table[idx] and self.table[idx][0] == key:
            return self.table[idx][1]
        raise KeyError(f"Key {key} not found")

ht = HashTable(10)
ht.set("Bob", 25)
print(ht.get("Bob"))  # Output: 25
