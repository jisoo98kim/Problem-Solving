# Link: https://www.acmicpc.net/source/40413017

N = int(input())        # number of subjects
num_list = list(map(int, input().split()))

M = max(num_list)
for i in range(N):
    num_list[i] = num_list[i] / M * 100
avg = sum(num_list) / N

print(avg)
