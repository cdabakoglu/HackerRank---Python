n, m = map(int, input().split())
elementsOfArray = list(map(int, input().split()))

A = set(map(int, input().split()))
B = set(map(int, input().split()))

print(sum((i in A) - (i in B) for i in elementsOfArray))

# Caner Dabakoglu
# GitHub: https://github.com/cdabakoglu
