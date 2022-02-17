#Link: https://www.acmicpc.net/source/40401640

import sys
N = int(sys.stdin.readline())
num = N                                         # copy N to num. Variable.
cycle = 0

while 1:                                        # while true
    sum_num = (num // 10) + (num % 10)          # tens' digit + unit digit
    new_num = ((num % 10) * 10) + (sum_num % 10)
    cycle += 1                                  # +1 cycle completed
    if (new_num == N):
        break
    num = new_num

print(cycle)
