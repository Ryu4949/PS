import heapq
import sys
input = sys.stdin.readline

N = int(input())
problems = []
for _ in range(N):
    d, c = map(int, input().split())
    problems.append((d, c))

problems.sort()
noodles = []

for problem in problems:
    heapq.heappush(noodles, problem[1])
    if problem[0] < len(noodles):
        heapq.heappop(noodles)

print(sum(noodles))