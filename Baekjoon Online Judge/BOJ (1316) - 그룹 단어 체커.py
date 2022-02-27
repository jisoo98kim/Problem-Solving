# Link: https://www.acmicpc.net/source/40581391

N = int(input())
# copy the number of words
count = N

for __ in range(N):
    word = input()

    # the index of last letter is i+1, so repeat til len(word) - 1, or range(1, len(word)) -> compare indices i-1 and i
    for i in range(len(word) - 1):
        # compare two adjacent letters with .find() to find the index where that letter is first used
        if word.find(word[i]) > word.find(word[i+1]):
            count -= 1
            break

print(count)
