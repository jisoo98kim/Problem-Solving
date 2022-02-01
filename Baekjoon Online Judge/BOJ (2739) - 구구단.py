# Link: https://www.acmicpc.net/source/38386753

if __name__ == '__main__':
    N = int(input())

    i = 1
    while i < 10:
        result = N * i
        print(N, '*', i, '=', result)
        i += 1
