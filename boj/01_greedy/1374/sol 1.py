import heapq
import sys
input = sys.stdin.readline

N = int(input())
lectures = [[*map(int, input().split())] for _ in range(N)]
lectures.sort(key=lambda x: x[1])
classroom = []

for lecture in lectures:
    if not classroom:
        heapq.heappush(classroom, lecture[2])
    else:
        last = heapq.heappop(classroom)
        heapq.heappush(classroom, lecture[2])
        if lecture[1] < last:
            heapq.heappush(classroom, last)

print(len(classroom))