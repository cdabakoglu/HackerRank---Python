list1 = []

for _ in range(int(input())):
    list1.append([input(), float(input())])

newList = sorted(list(set([y for x,y in list1])))
second = newList[1]

for a,b in sorted(list1):
    if b == second:
        print(a)
        
        
/*
Caner Dabakoğlu
GitHub: https://github.com/cdabakoglu
*/
