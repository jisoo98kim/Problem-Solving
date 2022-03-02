# Link: https://www.acmicpc.net/source/40723130

N, target = map(int, input().split())
num_list = list(map(int, input().split()))
low, high = 0, 0
sum = num_list[low]
length = N + 1

while low <= high:
    if sum >= target:
        length = min(length, high - low + 1)

        sum -= num_list[low]
        low += 1

        if low == N:
            break

    elif sum < target:
        high += 1

        if high == N:
            break

        sum += num_list[high]

if length == N + 1:
    length = 0

print(length)
