#Link: https://www.acmicpc.net/source/39133575

N = int(input())

for i in range(1, N + 1):
    print(' ' * (N - i) + '*' * i) # align right
