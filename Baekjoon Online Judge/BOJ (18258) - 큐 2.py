# Link: https://www.acmicpc.net/source/41318853

import sys
from collections import deque
n = int(sys.stdin.readline())
que = deque()

for i in range(n):
    command = sys.stdin.readline().split()
    # push X: 정수 X를 큐에 넣는 연산이다.
    if command[0] == 'push':
        que.append(command[1])
    # pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다.
    # 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif command[0] == 'pop':
        if que:
            print(que[0])
            que.popleft()
        else:
            print(-1)
    # size: 큐에 들어있는 정수의 개수를 출력한다.
    elif command[0] == 'size':
        print(len(que))
    # empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
    elif command[0] == 'empty':
        print(1 if not que else 0)
    # front: 큐의 가장 앞에 있는 정수를 출력한다.
    # 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif command[0] == 'front':
        print(que[0] if que else -1)
    # back: 큐의 가장 뒤에 있는 정수를 출력한다.
    # 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif command[0] == 'back':
        print(que[-1] if que else -1)
