# Link: https://www.acmicpc.net/source/41110540

import sys

xlist = []
ylist = []
for __ in range(3):
    x, y = map(int, sys.stdin.readline().split())
    xlist.append(x)
    ylist.append(y)

# 숫자가 하나씩 나온 것을 찾는다
for i in range(3):
    if xlist.count(xlist[i]) == 1:
        x4 = xlist[i]
    if ylist.count(ylist[i]) == 1:
        y4 = ylist[i]
# 정답 출력
print(x4, y4)
