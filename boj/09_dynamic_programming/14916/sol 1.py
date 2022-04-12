N = int(input())
INF = 100001
dp = [INF] * (N+5)
dp[2] = 1
dp[5] = 1
dp[4] = 2

for i in range(6, N+1):
    dp[i] = min(dp[i-2]+1, dp[i-5]+1)

if dp[N] >= INF:
    print(-1)
else:
    print(dp[N])