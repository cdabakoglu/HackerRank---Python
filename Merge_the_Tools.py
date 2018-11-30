import textwrap
import collections

def merge_the_tools(string, k):
    t = textwrap.wrap(string, k)

    for i in t:
        print(''.join(collections.OrderedDict.fromkeys(i).keys()))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
    
    
# Caner Dabakoglu
# GitHub: https://github.com/cdabakoglu
