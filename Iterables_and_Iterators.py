from itertools import combinations

N = int(input())
letterList = input().split()
K = int(input())

comb = list(combinations(letterList, K))

contains = 0

for i in comb:
    if 'a' in i:
        contains += 1

print("{:.3f}".format(contains / len(comb)))


# Caner Dabakoglu
# GitHub: https://github.com/cdabakoglu
