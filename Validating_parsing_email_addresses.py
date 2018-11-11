import email.utils
import re
N=int(input())

for i in range(N):
    new = email.utils.parseaddr(input())
    if re.match(r'[a-z](\w|\.|-)*@[a-z]+\.[a-z]{1,3}$', new[1]):
        print(email.utils.formataddr(new))
        
# Caner Dabakoğlu
# GitHub: https://github.com/cdabakoglu
