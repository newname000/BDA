import random

class FlajoletMartin:
    def __init__(self, num_hashes):
        self.num_hashes = num_hashes
        self.seeds = [random.randint(0, 2**32) for _ in range(num_hashes)]
        self.max_zeros = [0] * num_hashes

    def add(self, item):
        for i, seed in enumerate(self.seeds):
            hash_value = hash((seed, item))
            leading_zeros = (hash_value ^ (hash_value - 1)).bit_length() - 1
            self.max_zeros[i] = max(self.max_zeros[i], leading_zeros)

    def estimate(self):
        total = 0
        for zeros in self.max_zeros:
            total += 1 / (2 ** zeros)
        return int(self.num_hashes / total)

# Usage
flajolet_martin = FlajoletMartin(num_hashes=10)

# Simulating adding a few items to the stream
stream_items = [random.randint(0, 1000) for _ in range(10)]
for item in stream_items:
    flajolet_martin.add(item)
    print(f"Added '{item}' to the stream.")

# Final Output
estimate = flajolet_martin.estimate()
print(f"Estimated number of distinct elements: {estimate}")

