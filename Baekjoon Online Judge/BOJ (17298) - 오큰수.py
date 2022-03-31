# Link: https://www.acmicpc.net/source/41281295

import sys
n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))

stack = []
# result는 -1로 초기화
result = [-1] * n

for i in range(n):
    # stack은 값이 아닌 인덱스를 활용
    while stack and num_list[stack[-1]] < num_list[i]:
        # result의 stack.pop()한 자리에 num_list[i]를 넣어줌
        result[stack.pop()] = num_list[i]
    stack.append(i)

# *: 공백을 기준으로 원소들 프린트
print(*result)
