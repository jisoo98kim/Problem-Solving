# Link: https://www.acmicpc.net/source/40937719

import math

M, N = map(int, input().split())

def is_prime(num):
    if num > 1: # 1 != prime num
        for x in range(2, int(math.sqrt(num)) + 1):
            if num % x == 0:  # not a prime number
                return False
        return True

if __name__ == '__main__':
    for i in range(M, N + 1):
        if is_prime(i):
            print(i)

