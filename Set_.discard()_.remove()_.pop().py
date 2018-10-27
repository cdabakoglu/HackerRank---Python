n = int(input())
s = set(map(int, input().split()))

N = int(input())

for i in range(N):
    T = input().split()
   
    if T[0] == "remove":
        s.remove(int(T[1]))
    elif T[0] == "discard":
        s.discard(int(T[1]))
    else:
        s.pop()
    

print(sum(s))


# Caner Dabakoğlu
# GitHub: https://github.com/cdabakoglu
