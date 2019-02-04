from itertools import product

K, M = map(int, input().split())

numbers = list()

for i in range(K):
    N = list(map(int, input().split()))
    if len(N) >= N[0]:
        numbers.append(N[1:])

results = list(map(lambda x: sum(i ** 2 for i in x)%M, product(*numbers)))

print(max(results))

# Caner Dabakoglu
# GitHub: https://github.com/cdabakoglu
