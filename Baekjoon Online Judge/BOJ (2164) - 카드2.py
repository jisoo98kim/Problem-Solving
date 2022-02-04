# Link: https://www.acmicpc.net/source/38557829

from collections import deque   # Using deque
N = int(input())        # num. of cards
cards = deque([i for i in range(1, N + 1)])     # List Comprehension

while len(cards) > 1:
    cards.popleft()     # Remove the top card
    cards.append(cards.popleft())   # Move the top card to the bottom

print(cards[0])
