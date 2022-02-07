#Link: https://www.acmicpc.net/source/39068278

import sys
T = int(input())

for _ in range(T):
    a, b = map(int, sys.stdin.readline().split(' '))
    print(a + b)
