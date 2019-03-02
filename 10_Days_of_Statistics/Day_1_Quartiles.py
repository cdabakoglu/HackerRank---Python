from statistics import median

N = int(input())
X = sorted(list(map(int, input().split())))

if N % 2 == 0:
    lower = X[:N//2]
    upper = X[N//2:]
else:
    lower = X[:N//2]
    upper = X[N//2+1:]

print(int(median(lower)), int(median(X)), int(median(upper)), sep = "\n")


# Caner Dabakoğlu
# GitHub: https://github.com/cdabakoglu
