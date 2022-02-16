#Link: https://www.acmicpc.net/source/39214769

import sys

while True:
    try:
        A, B = map(int, sys.stdin.readline().split())
        print(A + B)
    except:
        break
