# Link: https://www.acmicpc.net/source/40956219

def fact(n):
    # for n = 0 or n = 1
    ans = 1
    if n > 0:
        ans = n * fact(n - 1)
    return ans


if __name__ == '__main__':
    n = int(input())
    print(fact(n))
