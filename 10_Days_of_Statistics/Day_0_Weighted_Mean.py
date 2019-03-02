N = int(input())
X = list(map(int, input().split()))
W = list(map(int, input().split()))

numerator = 0;
denominator = 0;

for i in range(N):
    numerator += X[i]*W[i]
    denominator += W[i]

print("{:.1f}".format(numerator / denominator))

# Caner Dabakoglu
# GitHub: https://github.com/cdabakoglu
