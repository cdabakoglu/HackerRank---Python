from collections import OrderedDict

N = int(input())
dictionaryPrice = OrderedDict()
dictionaryQuantity = OrderedDict()

for i in range(N):
    a = input().rsplit(' ', 1)
    if a[0] in dictionaryQuantity.keys():
        dictionaryQuantity[a[0]] += 1
    else:
        dictionaryQuantity[a[0]] = 1

    if a[0] not in dictionaryPrice.keys():
        dictionaryPrice[a[0]] = a[1]
    
fruits = list(dictionaryPrice.keys())
quantity = list(dictionaryQuantity.values())
price = list(dictionaryPrice.values())

for i in range(len(fruits)):
    print(fruits[i] + " " + str(int(quantity[i])*int(price[i])))
    
    
# Caner Dabakoğlu
# GitHub: https://github.com/cdabakoglu
