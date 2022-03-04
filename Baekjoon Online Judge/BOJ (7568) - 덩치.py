# Link: https://www.acmicpc.net/source/40744446

N = int(input())                                # N: num. of people
people_list = []

for __ in range(N):
    w, h = map(int, input().split())            # w: weight, h: height
    people_list.append((w, h))

for i in people_list:
    rank = 1                                    # set the default to 1
    for j in people_list:
        if i[0] < j[0] and i[1] < j[1]:         # condition given
            rank += 1
    print(rank, end = " ")


