from statistics import median

n = int(input())
X = list(map(int, input().split()))
F = list(map(int, input().split()))
S = list()

for i in range(n):
    for j in range(F[i]):
        S.append(X[i])

t = len(S) // 2
S.sort()

if t % 2 == 0:
    lower = S[:t]
    upper = S[t:]
else:
    lower = S[:t]
    upper = S[t+1:]

print(round(float(median(upper) - median(lower)),1))


# Caner Dabakoglu
# GitHub: https://github.com/cdabakoglu
