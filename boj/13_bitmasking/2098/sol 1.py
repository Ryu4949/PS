#시간초과

import sys
input = sys.stdin.readline

def travel(start, last, cost, visited):
    global ans

    if cost >= ans:
        return

    if visited == (1<<N)-1:
        if costs[last][start]:
            ans = min(ans, cost+costs[last][start])
        return

    for j in range(N):
        if visited & (1<<j):
            continue
        if not costs[last][j]:
            continue

        travel(start, j, cost+costs[last][j], visited|(1<<j))

N = int(input())
costs = [[*map(int, input().split())] for _ in range(N)]
ans = 10**8

travel(0, 0, 0, 1)

print(ans)