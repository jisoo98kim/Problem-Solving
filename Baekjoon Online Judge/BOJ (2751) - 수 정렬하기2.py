# Link: https://www.acmicpc.net/source/38499664
# pypy3

N = int(input()) # How many numbers

collect = [i for i in range(N)] # List comprehension

# save numbers to the list "collect"
for i in collect:
    collect[i] = int(input())

for i in sorted(collect):
    print(i)
