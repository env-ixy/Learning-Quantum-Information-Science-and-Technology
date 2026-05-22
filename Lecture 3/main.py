import numpy as np


ket0 = np.array([[1], [0]])
bra0 = np.array([[1, 0]])
print((bra0 @ ket0).item()) # [[1]]

bra1 = np.array([[0, 1]])
ket1 = np.array([[0], [1]])
print((bra1 @ ket1).item()) # [[1]]