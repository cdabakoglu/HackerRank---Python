import re

N = int(input())

for i in range(N):
    i = input()
    i = re.sub(r"(?<= )&&(?= )", "and", i)
    i = re.sub(r"(?<= )\|\|(?= )", "or", i)
    print(i)
    
    
# Caner Dabakoglu
# GitHub: https://github.com/cdabakoglu
