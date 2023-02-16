import numpy as np

A = [[24, 5, 78],
    [2, 54, 4],
    [34, 89, 54]]

B = [[44, 67, 99],
    [23, 4, 0],
    [49, 33, 11]]

result = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

result = np.dot(A, B)

for r in result:
    print(r)