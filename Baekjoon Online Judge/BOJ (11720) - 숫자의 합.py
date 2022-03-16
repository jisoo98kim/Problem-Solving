# Link: https://www.acmicpc.net/source/41009314

# Solution 1

# 유저 인풋 받기
n = int(input())
nums = list(map(int, input()))

sum = 0
for idx in nums:
    sum += idx
print(sum)

# Solution 2

# n = int(input())
# print(sum(map(int, input())))

