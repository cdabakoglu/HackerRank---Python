N,M = map(int, input().split())

for i in range(1, N, 2):
    print((i * '.|.').center(M, '-'))

print('WELCOME'.center(M, '-'))

for j in range(N-2, 0, -2):
    print((j * '.|.').center(M, '-'))
    
    
# Caner Dabakoğlu
# GitHub: https://github.com/cdabakoglu
