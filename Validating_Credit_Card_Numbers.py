import re

filters = r"^(?!.*(\d)(-?\1){3})[4-6]{1}\d{3}(?:-?\d{4}){3}$"

N = int(input())

for i in range(N):
    item = input()
    if re.search(filters, item):
        print("Valid")
    else:
        print("Invalid") 


# Caner Dabakoğlu
# GitHub: https://github.com/cdabakoglu
