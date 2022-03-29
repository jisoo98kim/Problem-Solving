# Link: https://www.acmicpc.net/source/41171281

import sys
from math import sqrt

# 에라토스테네스의 체 이용 (미리 모든 소수 구하기)
N = 123456 * 2 + 1
sieve = [True] * N
for i in range(2, int(sqrt(N)) + 1):
    if sieve[i]:
        for j in range(2 * i, N, i):
            sieve[j] = False

# 베르트랑 공준 (Bertrand's postulate)
def cnt_prime(n):
    cnt = 0
    for i in range(n + 1, 2 * n + 1):
        if sieve[i]:
            cnt += 1
    print(cnt)

while True:
    n = int(sys.stdin.readline())
    # 0이 입력되면 멈춤
    if n == 0:
        break
    cnt_prime(n)
