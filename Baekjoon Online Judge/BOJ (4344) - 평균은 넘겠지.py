# Link: https://www.acmicpc.net/source/40528419

C = int(input())

for __ in range(C):
    test_list = list(map(int, input().split()))
    N = test_list[0]                                # N = num of students in this test case
    avg = sum(test_list[1:]) / N

    count = 0
    for score in test_list[1:]:
        if score > avg:
            count += 1                              # num of students with scores higher than the avg
        rate = count / N * 100                      # % of students with scores above avg

    print('%.3f' %rate + '%')                       # print result up to 3 decimal place


