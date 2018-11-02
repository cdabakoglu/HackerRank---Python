cube = lambda x : x**3 

def fibonacci(n):
    fiboList = []
    a = 0
    b = 1
    while len(fiboList) < n:
        fiboList.append(a)
        a,b = b, a+b
    return(fiboList)


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
    
    
# Caner Dabakoğlu
# GitHub: https://github.com/cdabakoglu
