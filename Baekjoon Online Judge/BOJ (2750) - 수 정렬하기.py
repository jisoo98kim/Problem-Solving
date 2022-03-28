# Link: https://www.acmicpc.net/source/41124541

test_case = int(input())
num_list = []

for __ in range(test_case):
    num_list.append(int(input()))

# Bubble Sort
for i in range(len(num_list)):
    for j in range(len(num_list)):
        if num_list[i] < num_list[j]:
            num_list[i], num_list[j] = num_list[j], num_list[i]

for x in num_list:
    print(x)
