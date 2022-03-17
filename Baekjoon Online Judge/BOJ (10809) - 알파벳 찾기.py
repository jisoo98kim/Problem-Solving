# Link: https://www.acmicpc.net/source/41026172

word = input()

# Solution 1

# 범위: 아스키코드 a~z
alpha = list(range(97, 123))

for i in alpha:
    print(word.find(chr(i)), end = ' ')

# Solution 2

# alpha = 'abcdefghijklmnopqrstuvwxyz'
# for i in alpha:
#     print(word.find(i), end = ' ')
