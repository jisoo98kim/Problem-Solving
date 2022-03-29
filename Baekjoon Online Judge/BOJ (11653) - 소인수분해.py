# Link: https://www.acmicpc.net/source/41172804

import sys
n = int(sys.stdin.readline())

# 소인수분해
for i in range(2, int(n ** 0.5) + 1):
    while n % i == 0:
        print(i)
        n //= i

if n > 1:
    print(n)

