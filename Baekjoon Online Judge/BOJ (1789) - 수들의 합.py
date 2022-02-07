#Link: https://www.acmicpc.net/source/39027896

S = int(input())
N = 1

while N * (N + 1) / 2 <= S:     # Use Sum of Natural Numbers formula
    N += 1
print(N - 1)
