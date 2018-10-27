import re

T = int(input())

i = 0
while i < T:
    S = input()
    try:
        re.compile(S.strip())
        print(True)

    except re.error:
        print(False)
    
    i += 1


# Caner Dabakoğlu
# GitHub: https://github.com/cdabakoglu
