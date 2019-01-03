from collections import OrderedDict

n = int(input())

d = OrderedDict()

for i in range(n):
    w = input()
    if w in d:
        d[w] += 1
    else:
        d[w] = 1

totalNumber = len(d)
occur = []

for j in d.values():
    occur.append(str(j))
    
occ = ' '.join(occur)

print("{}\n{}".format(totalNumber, occ))


# Caner Dabakoglu
# GitHub: https://github.com/cdabakoglu
