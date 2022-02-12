#Link: https://www.acmicpc.net/source/39132883

T = int(input())

for nums in range(1, T + 1):
    a, b = map(int, input().split(' '))
    c = a + b
    print(f'Case #{nums}: {a} + {b} = {c}') # print in "Case #x: A + B = C" format
