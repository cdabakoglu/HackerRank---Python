import string

def print_rangoli(size):
    letters = string.ascii_lowercase
    bottomList = []
    topList = []
    width = 4*size - 3

    for i in range(size):
        x = "-".join(letters[i:size])
        topList.append(x[::-1]+x[1:])

    topList.pop(0)
    for i in reversed(topList):
        print(i.center(width, "-"))
    

    for i in range(size):
        x = "-".join(letters[i:size])
        bottomList.append(x[::-1]+x[1:])
        print (bottomList[i].center(width, "-"))

    

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
    
    
# Caner Dabakoğlu
# GitHub: https://github.com/cdabakoglu
