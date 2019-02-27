import numpy as np
from scipy import stats

N = int(input())
X = list(map(int, input().split()))

print("{:.1f}".format(np.mean(X)))
print("{:.1f}".format(np.median(X)))
print("{:.1f}".format(stats.mode(X)[0][0]))


# Caner Dabakoglu
# GitHub: https://github.com/cdabakoglu
