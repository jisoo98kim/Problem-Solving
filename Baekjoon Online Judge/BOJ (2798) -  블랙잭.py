# Link: https://www.acmicpc.net/source/38447368

from itertools import combinations

N, M = map(int, input().split(' ')) # N: num of cards, M: Max num
card_list = list(map(int, input().split(' '))) # Collect the cards as a list
max_sum = 0

for i in combinations(card_list,3): # choose 3 from card_list
    if sum(i) <= M:
        max_sum = max(max_sum, sum(i)) # compare two sums and set the max as max_sum
print(max_sum)
