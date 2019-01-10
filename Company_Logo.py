from collections import OrderedDict, Counter

S = Counter(input())

S = sorted(S.items(), key = lambda x: x[0])
S = sorted(S, key = lambda x: x[1], reverse=True)

for k,v in S[:3]:
    print(k,v)
    
    
# Caner Dabakoğlu
# GitHub: https://github.com/cdabakoglu
