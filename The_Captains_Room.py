K = int(input())
rooms = list(map(int, input().split()))
setRooms = set(rooms)

print(((sum(setRooms)*K)-sum(rooms)) // (K-1))


# Caner Dabakoğlu
# GitHub: https://github.com/cdabakoglu
