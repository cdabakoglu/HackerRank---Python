if __name__ == '__main__':
    N = int(input())

newList = []
for i in range(0,N):
    inputs = input().split()

    if inputs[0] == "insert":
        newList.insert(int(inputs[1]), int(inputs[2]))
    elif inputs[0] == "print":
        print(newList)
    elif inputs[0] == "remove":
        newList.remove(int(inputs[1]))
    elif inputs[0] == "append":
        newList.append(int(inputs[1]))
    elif inputs[0] == "sort":
        newList.sort()
    elif inputs[0] == "pop":
        newList.pop()
    elif inputs[0] == "reverse":
        newList.reverse()
        
        
 # Caner Dabakoğlu
 # GitHub: https://github.com/cdabakoglu
