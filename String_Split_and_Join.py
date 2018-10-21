def split_and_join(line):
    splitList = line.split()
    joinString = "-".join(splitList)
    return joinString
    
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
    
    
# Caner Dabakoğlu
# GitHub: https://github.com/cdabakoglu
