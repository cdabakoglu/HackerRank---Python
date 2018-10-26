T = int(input())
for i in range(T):

    try:
        a, b = map(int, input().split())
        print(int(a)//int(b))
    except (ZeroDivisionError, ValueError) as e:
        print("Error Code:",e)
        
        
# Caner Dabakoğlu
# GitHub: https://github.com/cdabakoglu
