# Link: https://www.acmicpc.net/source/41243549

import sys

k = int(input())
stack = []

for i in range(k):
    n = int(sys.stdin.readline())
    # 가장 최근에 쓴 수 지우기
    if n == 0:
        stack.pop()
    else:
        stack.append(n)
print(sum(stack))
