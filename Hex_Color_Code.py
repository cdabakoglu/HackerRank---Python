import re

N = int(input())
m = []
for i in range(N):
    m.append(re.findall(r':?.(#[A-Fa-f0-9]{6}|#[A-Fa-f0-9]{3})', input()))

for i in m:
    if i != []:
        for j in i:
            print(j)
        

# Caner Dabakoğlu
# https://github.com/cdabakoglu
