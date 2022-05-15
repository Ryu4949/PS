#시간초과

import heapq

heap1 = []
heap2 = []

N = int(input())
for _ in range(N):
    num = int(input())
    if len(heap1) <= len(heap2):
        if heap2 and num > heap2[0]:
            heapq.heappush(heap2, num)
            heapq.heappush(heap1, -heapq.heappop(heap2))
        else:
            heapq.heappush(heap1, -num)
    else:
        if num >= -heap1[0]:
            heapq.heappush(heap2, num)
        else:
            heapq.heappush(heap1, -num)
            heapq.heappush(heap2, -heapq.heappop(heap1))

