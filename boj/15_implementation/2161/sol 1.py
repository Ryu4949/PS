from collections import deque

N = int(input())

cards = deque([i for i in range(1, N+1)])
discard = []

while cards:
    discard.append(cards.popleft())
    if cards:
        cards.append(cards.popleft())

print(*discard)