from bitarray import bitarray
import mmh3

class BloomFilter:
    def __init__(self, size, num_hashes):
        self.size = size
        self.num_hashes = num_hashes
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)

    def add(self, item):
        for seed in range(self.num_hashes):
            index = mmh3.hash(item, seed) % self.size
            self.bit_array[index] = 1

    def contains(self, item):
        for seed in range(self.num_hashes):
            index = mmh3.hash(item, seed) % self.size
            if not self.bit_array[index]:
                return False
        return True

# Example Usage
bloom_filter = BloomFilter(size=10, num_hashes=3)

words_to_add = ["apple", "banana", "cherry", "date"]
for word in words_to_add:
    bloom_filter.add(word)

word_to_check = "banana"
if bloom_filter.contains(word_to_check):
    print(f"{word_to_check} might be in the set.")
else:
    print(f"{word_to_check} is definitely not in the set.")

