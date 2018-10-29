from itertools import combinations_with_replacement

S,k = input().upper().split()
k = int(k)
newList = []
for i in S:
    newList.append(i)
newList.sort()
combList = list(combinations_with_replacement(newList, k))

for i in combList:
    print("".join(i))


# Caner Dabakoğlu
# GitHub: https://github.com/cdabakoglu
