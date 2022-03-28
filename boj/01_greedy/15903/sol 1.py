'''
그냥 그 순간 카드 뭉치에서 가장 작은 카드 두 장씩 꺼내서 덮어쓰는걸 반복하면 된다
힙을 쓰지 않으면 정렬하고 카드 꺼내서 넣고, 다시 정렬하는 과정을 반복해야하기에 비효율적이다
'''

import heapq

N, M = map(int, input().split())
card = list(map(int, input().split()))
heapq.heapify(card)

for _ in range(M):
    card1, card2 = heapq.heappop(card), heapq.heappop(card)
    new = card1 + card2
    heapq.heappush(card, new)
    heapq.heappush(card, new)

print(sum(card))