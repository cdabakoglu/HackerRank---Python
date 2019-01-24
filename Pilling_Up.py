T = int(input())

for i in range(T):
    n = int(input())
    sides = [int(number) for number in input().split()]
    a = 0
    while a < n-1 and sides[a] >= sides[a+1]:
        a += 1
    while a < n-1 and sides[a] <= sides[a+1]:
        a += 1
    if a == n-1:
        print("Yes")
    else:
        print("No")
