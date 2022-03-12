# Link: https://www.acmicpc.net/source/40967817

a, b, c = map(int, input().split())
# a: 고정비용, b: 가변비용, c: 노트북 가격

# 손익분기점 : a + b * n < c * n
#           a < (c * n) - (b * n)
#           a < (c - b) * n
#           a // (c - b) < n

# 손익분기점 존재 x
if b >= c:
    print(-1)
else:
    print((a // (c - b)) + 1)


