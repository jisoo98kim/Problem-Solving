# Link: https://www.acmicpc.net/source/41105182

test_case = int(input())

for i in range(test_case):
    h, w, n = map(int, input().split())
    floor = (n % h) * 100
    num = n // h + 1

    # 예외 값: h의 배수일 경우
    if n % h == 0:
        floor = h * 100
        num = n // h
    print(floor + num)
