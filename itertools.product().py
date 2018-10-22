import itertools

A = input()
B = input()

def cartes(A,B):
    AList = A.split()
    BList = B.split()
    AList = list(map(int, AList))
    BList = list(map(int, BList))


    result = list(itertools.product(AList, BList))
    for i in result:
        print(i,end=' ')

cartes(A,B)

# Caner Dabakoğlu
# GitHub: https://github.com/cdabakoglu
