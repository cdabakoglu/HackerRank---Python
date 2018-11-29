import numpy as np

arrayA = np.array(list(map(int, input().split())))
arrayB = np.array(list(map(int, input().split())))

print(np.inner(arrayA, arrayB))
print(np.outer(arrayA, arrayB))

# Caner Dabakoglu
# GitHub: https://github.com/cdabakoglu
