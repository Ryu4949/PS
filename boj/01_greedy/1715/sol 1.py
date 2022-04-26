import heapq

N = int(input())
cards = [int(input()) for _ in range(N)]
heapq.heapify(cards)

ans = 0
for _ in range(N-1):
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    heapq.heappush(cards, a+b)
    ans += (a+b)

print(ans)