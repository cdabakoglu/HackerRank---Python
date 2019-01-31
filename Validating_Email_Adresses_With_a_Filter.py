import re

filters = re.compile('(^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{0,3}$)')
def fun(s):
    # return True if s is a valid email, else return False
    if bool(re.match(filters, s)):
        return True
    else:
        return False

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)


# Caner Dabakoglu
# GitHub: https://github.com/cdabakoglu
