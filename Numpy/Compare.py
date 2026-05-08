import numpy as np

#comparison operator

scores = np.array([91, 55, 100, 73, 82, 64])

# print(scores< 0)
scores[scores < 60] = 0
print(scores)