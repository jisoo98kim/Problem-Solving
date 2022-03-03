# Link: https://www.acmicpc.net/source/40743228

N = int(input())
result = 0

for num in range(1, N + 1):
    arr = list(map(int, str(num)))
    new_sum = num + sum(arr)
    if (new_sum == N):
        result = num
        break

print(result)

