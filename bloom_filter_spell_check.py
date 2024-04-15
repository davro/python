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

# Example Usage for Spell Checking
def build_spell_check_bloom_filter(word_list, filter_size, num_hashes):
    bloom_filter = BloomFilter(size=filter_size, num_hashes=num_hashes)
    for word in word_list:
        bloom_filter.add(word)
    return bloom_filter

# Example dictionary of words
dictionary = ["apple", "banana", "cherry", "date", "grape", "kiwi", "orange", "pear", "pineapple", "strawberry"]

# Build the Bloom filter for spell checking
spell_check_filter = build_spell_check_bloom_filter(dictionary, filter_size=1000, num_hashes=5)

# Test spell checking
words_to_check = ["apple", "kiwi", "watermelon", "strawberry", "peach"]

for word in words_to_check:
    if spell_check_filter.contains(word):
        print(f"{word} is likely spelled correctly.")
    else:
        print(f"{word} may be misspelled.")

# Additional words not in the dictionary
additional_words = ["xylophone", "quasar", "zygote"]

print("\nAdditional Words:")
for word in additional_words:
    if spell_check_filter.contains(word):
        print(f"{word} is likely spelled correctly.")
    else:
        print(f"{word} may be misspelled.")

