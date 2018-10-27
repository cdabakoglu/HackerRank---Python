from itertools import combinations

S = input().upper()

newList = S.split()
word = "".join(sorted(newList[0]))
number = int(newList[1])

resultList = list()

i = 1
while i <= number:
    for a in list(combinations(word, i)):
        resultList.append(a)
    i += 1

for i in resultList:
    print("".join(i))
    
    
    
# Caner Dabakoğlu
# GitHub: https://github.com/cdabakoglu
