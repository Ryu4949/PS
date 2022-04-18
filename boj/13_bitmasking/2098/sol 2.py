import sys
input = sys.stdin.readline

N = int(input())
costs = [[*map(int, input().split())] for _ in range(N)]
INF = int(1e8)

dp = [[INF] * (1<<N) for _ in range(N)]

def travel(i, visited):
    if dp[i][visited] != INF:
        return dp[i][visited]

    if visited == (1<<N)-1:
        if costs[i][0]:
            return costs[i][0]
        else:
            return INF

    for j in range(1, N):
        if not costs[i][j]:
            continue

        if visited & (1 << j):
            continue

        dp[i][visited] = min(dp[i][visited], travel(j, visited|(1<<j))+costs[i][j])

    return dp[i][visited]

print(travel(0, 1))