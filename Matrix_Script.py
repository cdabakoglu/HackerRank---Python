import re

N, M = map(int, input().split())
matrix = []

for i in range(N):
    matrix.append(input())

matrix = list(zip(*matrix))

word = str()

for a in matrix:
    for b in a:
        word += b

print(re.sub(r'(?<=\w)([^\w\d]+)(?=\w)', ' ', word))
