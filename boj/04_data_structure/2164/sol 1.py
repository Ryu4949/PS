from collections import deque

N = int(input())
cards = deque([i for i in range(1, N+1)])
total = N

while len(cards) > 1:
    discard = cards.popleft()
    move = cards.popleft()
    cards.append(move)

print(cards[0])