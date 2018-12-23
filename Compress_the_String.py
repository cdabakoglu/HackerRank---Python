from itertools import groupby

for i,j in groupby(input()):
    g=tuple((len(list(j)), int(i)))
    print(g, end=" ")
    
# Caner Dabakoglu
# GitHub: https://github.com/cdabakoglu
