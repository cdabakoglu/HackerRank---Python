T = int(input())

for i in range(T):
    aNumber, aSet, bNumber, bSet = (set(input().split()) for i in range(4))
    if set(aSet) < set(bSet):
        print("True")
    else:
        print("False")
        
# Caner Dabakoğlu
# GitHub: https://github.com/cdabakoglu
