# Link: https://www.acmicpc.net/source/41317340

from collections import deque
import sys
n = int(sys.stdin.readline())
deq = deque()

for i in range(n):
    c = sys.stdin.readline().split()
    # push_front X: 정수 X를 덱의 앞에 넣는다.
    if c[0] == 'push_front':
        deq.appendleft(c[1])
    # push_back X: 정수 X를 덱의 뒤에 넣는다.
    elif c[0] == 'push_back':
        deq.append(c[1])
    # pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다.
    # 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif c[0] == 'pop_front':
        if not deq:
            print(-1)
        else:
            print(deq[0])
            deq.popleft()
    # pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다.
    # 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif c[0] == 'pop_back':
        if not deq:
            print(-1)
        else:
            print(deq[-1])
            deq.pop()
    # size: 덱에 들어있는 정수의 개수를 출력한다.
    elif c[0] == 'size':
        print(len(deq))
    # empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
    elif c[0] == 'empty':
        print('1' if not deq else '0')
    # front: 덱의 가장 앞에 있는 정수를 출력한다.
    # 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif c[0] == 'front':
        print('-1' if not deq else deq[0])
    # back: 덱의 가장 뒤에 있는 정수를 출력한다.
    # 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif c[0] == 'back':
        print('-1' if not deq else deq[-1])
