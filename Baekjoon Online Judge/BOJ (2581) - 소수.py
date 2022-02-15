import sys
import math

def is_prime(num):
    if num > 1: # 1 is not a prime number
        # convert to int as the result of math.sqrt() is float
        # the biggest divisor should be math.sqrt(num)
        for x in range(2, int(math.sqrt(num)) + 1):
            if num % x == 0:  # not a prime number
                return False
        return True

M = int(sys.stdin.readline())    # M <= N
N = int(sys.stdin.readline())    # sys.stdin.readline() is faster than input()
prime = []  # create an empty list

# Using is_prime function to make a list of prime numbers
for i in range(M, N + 1):
    if is_prime(i) == True:
        prime.append(i)

# Print answers
if len(prime) != 0:
    print(sum(prime))
    print(min(prime))
else:
    print(-1)
