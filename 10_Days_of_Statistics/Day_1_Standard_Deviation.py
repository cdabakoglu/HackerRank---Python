N = int(input())
X = list(map(int, input().split()))

x_mean = sum(X) / N
variance = sum([(x - x_mean)**2 for x in X]) / N
std = variance ** 0.5

print('{:.1f}'.format(std))


# Caner Dabakoglu
# GitHub: https://github.com/cdabakoglu
