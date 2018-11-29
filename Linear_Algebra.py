import numpy as np

np.set_printoptions(legacy='1.13')
N = int(input())


rowList = list()

for i in range(N):
    row = list(map(float, input().split()))
    rowList.append(row)

print((np.linalg.det(np.array(rowList))))


# Caner Dabakoglu
# GitHub: https://github.com/cdabakoglu
