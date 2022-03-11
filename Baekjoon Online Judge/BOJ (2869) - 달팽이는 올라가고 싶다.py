# Link: https://www.acmicpc.net/source/40956725

import math

# a: 낮에 올라가기, b: 밤에 미끄러지기, v: 나무 막대의 높이 (m)
a, b, v = map(int, input().split())

day = math.ceil((v - a) / (a - b)) + 1
# math.ceil을 통해 소수점 자리를 올림
# ex) 3.2 days -> 4 days
# v = (a - b) * day + a    ==>    (a - b) * day = v - a
# 마지막에 a 만큼 올라간 하루를 +1

print(day)

