#Link: https://www.acmicpc.net/source/39214364

import sys

while True:
    A, B = map(int, sys.stdin.readline().split())
    if (A == 0 or B == 0):  # not to print 0 + 0
        break
    else:
        print(A + B)
