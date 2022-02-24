# Link: https://www.acmicpc.net/source/40526501

N = int(input())

for __ in range(N):
    ox_list = list(input())     # saving input as a list, so we can work with indices
    score = 0
    total_score = 0

    for ox in ox_list:
        if ox == 'O':
            score += 1
            total_score += score
        else:
            score = 0
    print(total_score)

