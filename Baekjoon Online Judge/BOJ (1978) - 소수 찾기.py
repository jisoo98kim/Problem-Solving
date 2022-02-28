# Link: https://www.acmicpc.net/source/40714903

import math

N = int(input())
arr = list(map(int, input().split()))
count = 0

for num in arr:
    if num > 1:
        flag = True
        for div in range(2, int(math.sqrt(num)) + 1):
            if num % div == 0:  # not a prime number
                flag = False
                break

        if flag:
            count += 1
print(count)
