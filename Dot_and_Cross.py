import numpy as np

N = int(input())

rowListA = list()
rowListB = list()
for i in range(N):
    row = list(map(int, input().split()))
    rowListA.append(row)
for j in range(N):
    row = list(map(int, input().split()))
    rowListB.append(row)

arrayA = np.array(rowListA)
arrayB = np.array(rowListB)

print(np.dot(arrayA,arrayB))


# Caner Dabakoglu
# GitHub: https://github.com/cdabakoglu
