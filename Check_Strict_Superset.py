A = set(input().split())
n = int(input())

count = 0
for i in range(n):
    newSet = set(input().split())

    if A > newSet:
        count += 1

if count >= n:
    print("True")
else:
    print("False")
    
    
    
# Caner Dabakoğlu
# GitHub: https://github.com/cdabakoglu
