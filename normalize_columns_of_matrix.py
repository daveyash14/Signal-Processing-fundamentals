import numpy as np
from sklearn.preprocessing import normalize

#x = np.array([[0, 1, 0, 0, 0, 0],
#             [1, 0, 0, 0, 0, 0],
#             [0, 1, 0, 0, 1, 1],
#             [1, 0, 0, 1, 1, 0],
#             [1, 1, 0, 0, 0, 1],
#             [0, 0, 1, 0, 1, 0]])

x = np.random.randint(10, size=(6,6))
print("\nPrinting matrix")
print(x)

x_norm = x / x.max(axis=0)
#x_norm = normalize(x, axis=0, norm='max')
print("\nPrinting normalized matrix.")
print(x_norm)
