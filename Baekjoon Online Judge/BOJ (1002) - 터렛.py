# Link: https://www.acmicpc.net/source/41119602

test_case = int(input())

# 두 원의 접점의 개수 구하기
for __ in range(test_case):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    # distance 공식 사용
    d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    # 두 원의 중심이 같을 때
    if d == 0:
        # 두 원의 크기가 같은 경우
        if r1 == r2:
            print(-1)
        # 한 원이 다른 원의 안에 있을 경우
        else:
            print(0)
    # 두 원의 중심이 다를 때
    else:
        if (r1 + r2 == d) or (abs(r2 - r1) == d):
            print(1)
        elif (abs(r1 - r2) < d) and (d < r1 + r2):
            print(2)
        else:
            print(0)
