from collections import Counter

x = int(input())    # Number of shoes
shoeSize = Counter(map(int, input().split()))  # Shoe Size
n = int(input())    # Number of customer

revenue = 0
for i in range(n):
    shoe, price = map(int, input().split())
    

    if shoeSize[shoe] > 0:
            revenue += price
            shoeSize[shoe] -= 1

print(revenue)
