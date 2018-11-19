import numpy

N = list(map(int, input().split()))
num = []
for i in range(N[0]):
    num.append(list(map(int, input().split())))

array = numpy.array(num)
print((array.T))
print(array.flatten())


# Caner Dabakoğlu
# GitHub: https://github.com/cdabakoglu
