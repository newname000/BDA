import math
import random

class DGIM:
    def __init__(self, N):
        self.N = N
        self.buckets = []

    def add(self, bit):
        if bit == 1:
            self.buckets.insert(0, (1, 1))
        self.compress()

    def compress(self):
        i = 0
        while i < len(self.buckets) - 2:
            if self.buckets[i][1] == self.buckets[i+1][1] == self.buckets[i+2][1]:
                self.buckets[i+1] = (self.buckets[i+1][0], self.buckets[i+1][1] * 2)
                self.buckets.pop(i+2)
            else:
                i += 1

    def query(self, k):
        size = 0
        sum_bits = 0
        for ts, bsize in self.buckets:
            if size + bsize <= k:
                sum_bits += bsize
                size += bsize
            else:
                sum_bits += (k - size) * (bsize // 2)
                break
        return sum_bits

dgim = DGIM(100)
stream = [random.randint(0, 1) for _ in range(100)]
print(f"Binary stream: {stream}")

for bit in stream:
    dgim.add(bit)

query_k = 10
approx_count = dgim.query(query_k)
print(f"Approximate count of 1's in the last {query_k} bits is {approx_count}")



