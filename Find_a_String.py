def count_substring(string, sub_string):
    total = 0
    for i in string:
        if sub_string in string:
            total += 1
            subIndex = string.find(sub_string)
            string = string[subIndex+1:]
    return total
        

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
    
    
# Caner Dabakoğlu
# GitHub: https://github.com/cdabakoglu
