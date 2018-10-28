a, A = (set(input().split()) for i in range(2))
N = int(input())

for i in range(N):
    task, newSet = (input().split() for i in range(2))
    if task[0] == "intersection_update":
        A.intersection_update(newSet)
    elif task[0] == "update":
        A.update(newSet)
    elif task[0] == "symmetric_difference_update":
        A.symmetric_difference_update(newSet)
    else:
        A.difference_update(newSet)
total = 0
for i in A:
    total += int(i)

print(total)


# Caner Dabakoğlu
# GitHub: https://github.com/cdabakoglu
