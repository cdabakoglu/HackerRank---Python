from collections import namedtuple
N = int(input())
sheet = namedtuple('sheet','ID,MARKS,CLASS,NAME')

students = []
columns = input()
columnsList = columns.split()
total = 0
for i in range(N):
    a = input()
    aList = a.split()
    x = columnsList.index('MARKS')
    total += int(aList[x])

print(total / N)


# Caner Dabakoğlu
# GitHub: https://github.com/cdabakoglu
