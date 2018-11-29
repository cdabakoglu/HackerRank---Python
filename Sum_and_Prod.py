import numpy as np

N,M = map(int, input().split())

rowList = list()

for i in range(N):
    row = list(map(int, input().split()))
    rowList.append(row)

array = np.array(rowList)

print(np.prod(np.sum(array, axis=0)))


# Caner Dabakoglu
# GitHub: https://github.com/cdabakoglu
