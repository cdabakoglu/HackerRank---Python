def average(array):
    heightSet = set()
    for i in array:
        i = int(i)
        heightSet.add(i)

    return sum(heightSet) / len(heightSet)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
    
    
    # Caner Dabakoğlu
    # https://github.com/cdabakoglu
