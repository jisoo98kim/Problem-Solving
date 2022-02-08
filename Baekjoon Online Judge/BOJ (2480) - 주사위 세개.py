#Link: https://www.acmicpc.net/source/39062761

a, b, c = map(int, input().split(' '))

if a == b == c:     # all same pips
    print(10000 + a * 1000)
elif a == b or a == c:  # two same pips
    print(1000 + a * 100)
elif b == c:    # two same pips
    print(1000 + b * 100)
else:   # no same pips
    print(max(a,b,c) * 100)
