# Link: https://www.acmicpc.net/source/41175114

import sys
n = int(sys.stdin.readline())

stack = []
for i in range(n):
    c = sys.stdin.readline().split()

    if c[0] == 'push':
        stack.append(c[1])
    elif c[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif c[0] == 'size':
        print(len(stack))
    elif c[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif c[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            # 맨 위 = 가장 마지막 순서
            print(stack[-1])

