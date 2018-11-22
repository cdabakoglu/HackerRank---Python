import numpy

n, m = map(int, input().split())
a = []
b = []

for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n):
    b.append(list(map(int, input().split())))

a = numpy.array(a).reshape(n,m)
b = numpy.array(b).reshape(n,m)

print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(a**b)


# Caner Dabakoğlu
# GitHub: https://github.com/cdabakoglu
