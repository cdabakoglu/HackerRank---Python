from collections import deque
N = int(input())
d = deque()
for i in range(N):
    task = input().split()

    if task[0] == "append":
        d.append(task[1])
    elif task[0] == "appendleft":
        d.appendleft(task[1])
    elif task[0] == "pop":
        d.pop()
    else:
        d.popleft()

for i in d:
    print(i,end=" ")
    
    
# Caner Dabakoğlu
# GitHub: https://github.com/cdabakoglu
