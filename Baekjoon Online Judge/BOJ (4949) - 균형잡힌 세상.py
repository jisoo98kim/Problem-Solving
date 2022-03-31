# Link: https://www.acmicpc.net/source/41277773

import sys

while True:
    # .rsrtrip() 사용해서 공백문자 지우기
    string = sys.stdin.readline().rstrip()
    stack = []
    flag = True

    # 입력의 종료 조건 '.'
    if string == '.':
        break

    for c in string:
        # 시작하는 괄호들은 stack에 넣어줌
        if c == '(' or c == '[':
            stack.append(c)
        elif c == ')':
            # stack이 비어있지 않고, 괄호 짝이 맞을 경우
            if stack and stack[-1] == '(':
                # stack을 비워줌
                stack.pop()
            else:
                flag = False
                break
        elif c == ']':
            # stack이 비어있지 않고, 괄호 짝이 맞을 경우
            if stack and stack[-1] == '[':
                # stack을 비워줌
                stack.pop()
            else:
                flag = False
                break

    # 프린트 "yes" 스택이 있지 않고, 플래그가 true일 경우
    print("yes" if flag and not stack else "no")
