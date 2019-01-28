S = input()

lower = list()
upper = list()
numeric = list()
odd_numeric = list()
even_numeric = list()

for i in S:
    if i.islower():
        lower.append(i)
    elif i.isupper():
        upper.append(i)
    else:
        numeric.append(i)
for i in sorted(numeric):
    if int(i) % 2 == 0:
        even_numeric.append(i)
    else:
        odd_numeric.append(i)

numeric = odd_numeric + even_numeric

print(''.join(sorted(lower)), ''.join(sorted(upper)), ''.join(numeric), sep="", end="")


# Caner Dabakoglu
# GitHub: https://github.com/cdabakoglu
