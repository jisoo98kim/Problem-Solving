# Link: https://www.acmicpc.net/source/41280022

import sys
n = int(sys.stdin.readline())
cnt = 1
stack = []
op = []
flag = True

for i in range(n):
    x = int(sys.stdin.readline())
    # 입력받은 x 이하 숫자까지 stack에 넣음
    while cnt <= x:
        stack.append(cnt)
        op.append('+')
        cnt += 1

    # 입력받은 x와 stack에 마지막으로 들어간 숫자가 같으면 빼줌
    if stack[-1] == x:
        stack.pop()
        op.append('-')

    # 수열을 만들 수 없을 경우
    else:
        flag = False
        break

if flag:
    for i in op:
        print(i)
else:
    print('NO')


