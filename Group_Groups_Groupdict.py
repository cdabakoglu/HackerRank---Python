import re

m = re.search(r'([a-zA-Z0-9]+)',input()).group()

found = False

i = 0
while i+1 < len(m):
    if m[i] == m[i+1]:
        found = True
        print(m[i])
        break
    else:
        i += 1

if not found:
    print(-1)
    

    
# Caner Dabakoğlu
# GitHub: https://github.com/cdabakoglu
