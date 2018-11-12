# At least 2 uppercase letter
# At least 3 digits
# It should only contain alphanumeric char.
# No char. should repeat
# Exactly 10 char.

import re
n = int(input())
# Conditions
def conditions(uid):
    uid = "".join(sorted(uid))
    twoUppercase = bool(re.search(r'[A-Z]{2,}', uid))
    threeDigits = bool(re.search(r'[0-9]{3,}', uid))
    onlyAlpha = bool(re.search(r'^\w{10}$', uid))
    noRepeat = bool(re.search(r'(.)\1', uid))
    if twoUppercase and threeDigits and onlyAlpha and len(uid) == 10 and not noRepeat:
        print("Valid")
    else:
        print("Invalid")

for i in range(n):
    a = input()
    conditions(a)
    
    
 # Caner Dabakoğlu
 # https://github.com/cdabakoglu
