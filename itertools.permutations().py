from itertools import permutations

x = input()

def perm(x):
    newList = list()
    wordNo = x.find(' ')
    word = x[:wordNo]
    no = int(x[wordNo+1:])
    for i in word:
        newList.append(i)
    newList = sorted(newList)
    permList = list(permutations(newList, no))

    for i in permList:
        print(''.join(i))
    
perm(x)


# Caner Dabakoğlu
# GitHub: https://github.com/cdabakoglu
