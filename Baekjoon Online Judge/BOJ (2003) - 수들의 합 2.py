# Link: https://www.acmicpc.net/source/40720770

N, target = map(int, input().split())
num_list = list(map(int, input().split()))
count = 0

low, high = 0, 0
total = num_list[low]

while True:
    if total == target:
        count += 1
        total -= num_list[low]
        low += 1

    elif total > target:
        total -= num_list[low]
        low += 1

    else:
        high += 1

        if high == N:
            break

        total += num_list[high]

print(count)
