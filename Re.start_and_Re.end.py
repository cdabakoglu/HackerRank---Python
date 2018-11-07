import re
S = input()
k = input()

newList = []

i = 0

while i < len(S):
    m = re.search(k,S[i:])
    if m != None and ((m.start()+i,m.end()+i-1) not in newList):
        tup = (m.start()+i,m.end()+i-1)
        newList.append(tup)
    i += 1

if newList == []:
    falseTup = (-1, -1)
    print(falseTup)
else:
    for i in newList:
        print(i)
        
        
        
# Caner Dabakoğlu
# GitHub: https://github.com/cdabakoglu
