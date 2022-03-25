# Link: https://www.acmicpc.net/source/41108113

import sys

while True:
    nums = list(map(int, sys.stdin.readline().split()))
    # 수가 0, 0, 0이면 스탑
    if sum(nums) == 0:
        break
    max_num = max(nums)
    # 빗변은 리스트에서 제외
    nums.remove(max_num)

    # 피타고라스의 정리
    if (nums[0] ** 2 + nums[1] ** 2) == (max_num ** 2):
        print('right')
    else:
        print('wrong')
