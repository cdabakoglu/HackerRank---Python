import re
regex = r'[789][0-9]{9}$'

N = int(input())
for i in range(N):
    if re.match(regex, input()):
       print("YES")
    else:
        print("NO")
        
        
# Caner Dabakoğlu
# GitHub: https://github.com/cdabakoglu
