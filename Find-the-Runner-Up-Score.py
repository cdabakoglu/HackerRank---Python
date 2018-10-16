n = int(input())
arr = map(int, input().split())

num = list(arr)
a = max(num)

while a == max(num):
    num.remove(max(num))

print(max(num))


# Caner Dabakoğlu
# GitHub: https://github.com/cdabakoglu
