m = int(input())
mList = input().split()
n = int(input())
nList = input().split()
mSet = set()
nSet = set()
for i in mList:
    mSet.add(i)
for i in nList:
    nSet.add(i)

difList = []

for i in mSet.difference(nSet):
    difList.append(int(i))
for i in nSet.difference(mSet):
    difList.append(int(i))
for i in sorted(difList):
    print (i)
    
    
    
# Caner Dabakoğlu
# GitHub: https://github.com/cdabakoglu
