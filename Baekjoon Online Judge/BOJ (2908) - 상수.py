# Link: https://www.acmicpc.net/source/41069979

n, s = input().split()
# string reverse
print(max(int(n[::-1]), int(s[::-1])))
