N, X = map(int,input().split())
scores = list()
for i in range(X):
    marks = list(map(float, (input().split())))
    scores.append(marks)
    
zippySum = list(map(sum, list(zip(*scores))))

for i in zippySum:
    print (i / X)


# Caner Dabakoğlu
# GitHub: https://github.com/cdabakoglu
