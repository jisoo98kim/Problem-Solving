# Link: https://www.acmicpc.net/source/41060593

test_case = int(input())

for i in range(test_case):
    r, s = list(map(str, input().split()))
    mult = int(r)
    p = []
    idx = 0
    while len(s) > idx:
        p.append(s[idx] * mult)
        idx += 1

    print(''.join(p))


