#!/bin/python3

import math
import os
import random
import re
import sys
from operator import itemgetter

N, M = map(int, input().split())

columns = []

for i in range(N):
    columns.append(list(map(int, input().split())))

K = int(input())

for rows in sorted(columns, key=itemgetter(K)):
    print(*rows)



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

# Caner Dabakoglu
# GitHub: https://github.com/cdabakoglu
