import numpy

N, M, P = map(int, input().split())
newList = []
newList2 = []
for i in range (N):
    numericList = list(map(int, input().split()))
    newList.append(numericList)

for i in range (M):
    numericList = list(map(int, input().split()))
    newList2.append(numericList)

array1 = numpy.array(newList).reshape((N,P))
array2 = numpy.array(newList2).reshape((M,P))

print(numpy.concatenate((array1,array2)))


# Caner Dabakoğlu
# GitHub: https://github.com/cdabakoglu
