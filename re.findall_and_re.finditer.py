import re

string = input().split()
string2 = "".join(string)

matchs = re.findall(r'(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])([AEIOUaeiou][AEIOUaeiou]+)[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]',string2)

if matchs == []:
    print(-1)
else:
    for i in matchs:
        print(i)
        

# Caner Dabakoğlu
# GitHub: https://github.com/cdabakoglu
