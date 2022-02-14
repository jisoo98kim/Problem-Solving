#Link: https://www.acmicpc.net/source/39134786

N, X = map(int, input().split()) # N: num. of int, X: the number we compare other numbers with
compare = list(map(int, input().split())) # split by space

for i in range(N):
    if compare[i] < X:
        print(compare[i], end = " ") # end = " " to print the result in one line

