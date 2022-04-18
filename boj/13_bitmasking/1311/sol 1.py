import sys
input = sys.stdin.readline

N = int(input())
costs = [[*map(int, input().split())] for _ in range(N)]
INF = int(1e6)

dp = [[INF] * (1<<N) for _ in range(N)]

def work(i, visited):
    if dp[i][visited] != INF:
        return dp[i][visited]

    if visited == (1<<N)-1:
        return 0

    for j in range(1, N):
        if not costs[i][j]:
            continue

        if visited & (1 << j):
            continue

        dp[i][visited] = min(dp[i][visited], work(j, visited|(1<<j))+costs[i][j])

    return dp[i][visited]

print(work(0, 1))