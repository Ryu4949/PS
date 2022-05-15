#표준 입력 차이로 시간초과 벗어남
import heapq
import sys
input = sys.stdin.readline

heap1 = []
heap2 = []

N = int(input())
for _ in range(N):
    num = int(input())
    if len(heap1) > len(heap2):
        heapq.heappush(heap2, num)
    else:
        heapq.heappush(heap1, -num)

    if heap1 and heap2 and -heap1[0] > heap2[0]:
        heapq.heappush(heap2, -heapq.heappop(heap1))
        heapq.heappush(heap1, -heapq.heappop(heap2))

    print(-heap1[0])

