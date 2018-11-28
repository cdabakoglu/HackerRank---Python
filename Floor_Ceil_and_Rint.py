import numpy as np

np.set_printoptions(sign=" ")

A = np.array(list(map(float, input().split())))
print(np.floor(A), np.ceil(A), np.rint(A), sep="\n")
