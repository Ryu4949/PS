#시간초과

import heapq
import sys
input = sys.stdin.readline

N = int(input())
problems = []
day = 0
for _ in range(N):
    d, c = map(int, input().split())
    problems.append((-c, -d))
    day = max(day, d)

heapq.heapify(problems)
noodles = 0

while day > 0:
    temp = []
    while problems:
        problem = heapq.heappop(problems)
        if -problem[1] >= day:
            noodles -= problem[0]
            break
        else:
            temp.append(problem)

    day -= 1
    for i in temp:
        heapq.heappush(problems, i)

print(noodles)
