import numpy as np

N, M = map(int, input().split())

rowList = list()

np.set_printoptions(sign=" ",legacy='1.13')

for i in range(N):
    row = list(map(int, input().split()))
    rowList.append(row)

array = np.array(rowList)

print(np.mean(array, axis = 1))
print(np.var(array, axis = 0))
print(np.std(array))


# Caner Dabakoglu
# GitHub: https://github.com/cdabakoglu
