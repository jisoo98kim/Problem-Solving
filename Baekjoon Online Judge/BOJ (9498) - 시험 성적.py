# Link: https://www.acmicpc.net/source/38559705

score = int(input())

if score >= 90:     # max test score 100
    print("A")
elif 80 <= score < 90:
    print("B")
elif 70 <= score < 80:
    print("C")
elif 60 <= score < 70:
    print("D")
else:   # score lower than 60
    print("F")
