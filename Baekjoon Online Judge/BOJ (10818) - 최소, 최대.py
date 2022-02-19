N = int(input())                                # number of integers
list_nums = list(map(int, input().split()))     # list of integers

# Solution 1: https://www.acmicpc.net/source/40405069
"""
max = list_nums[0]
min = list_nums[0]

for num in list_nums[1:]:
    if num > max:
        max = num
    elif num < min:
        min = num

print(min, max)
"""
# 480 ms


# Solution 2: https://www.acmicpc.net/source/40405190
print(min(list_nums), max(list_nums))
# 404 ms


# Solution 3: https://www.acmicpc.net/source/40405231
# list_nums.sort()
# print(list_nums[0], list_nums[-1])
# 736 ms


