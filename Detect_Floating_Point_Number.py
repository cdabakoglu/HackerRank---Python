import re

T = int(input())

for i in range(T):
    print(bool(re.findall("^[-+]?[0-9]*\.[0-9]+$",input())))
    
    
    
# Caner Dabakoğlu
# GitHub: https://github.com/cdabakoglu
