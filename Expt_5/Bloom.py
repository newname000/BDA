#pip install mmh3

from bitarray import bitarray

class BloomFilter:
    def __init__(self, size, hash_count):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)

    def add(self, item):
        for i in range(self.hash_count):
            index = hash(item + str(i)) % self.size
            self.bit_array[index] = 1
        print(f"Added '{item}' to the Bloom filter.")

    def check(self, item):
        for i in range(self.hash_count):
            index = hash(item + str(i)) % self.size
            if self.bit_array[index] == 0:
                return False
        return True

bloom = BloomFilter(100, 3)
items_to_add = ["hello", "world", "foo", "bar"]
items_to_check = ["hello", "baz"]

for item in items_to_add:
    bloom.add(item)

for item in items_to_check:
    if bloom.check(item):
        print(f"'{item}' is possibly in the Bloom filter.")
    else:
        print(f"'{item}' is definitely not in the Bloom filter.")
