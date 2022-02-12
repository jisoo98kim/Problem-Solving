#Link: https://www.acmicpc.net/source/39131968

T = int(input())

for nums in range(1, T + 1):
    a, b = map(int, input().split(' '))
    print(f'Case #{nums}: {a + b}') # using f-string to iterate nums with ordered indices

