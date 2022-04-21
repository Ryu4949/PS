from pprint import pprint

N = int(input())
dp = [[0]*(1<<10) for _ in range(10)]

for i in range(1, 10):
    dp[i][1<<i] = 1

for _ in range(N):
    for i in range(10):
        for j in range(1<<10):
            if (1<<i) & j:
                if i == 0:
                    dp[i+1][j|(1<<(i+1))] = dp[i][j]+1
                elif i == 9:
                    dp[i-1][j|(1<<0)] = dp[i][j]+1
                else:
                    dp[i-1][j|(1<<(i-1))] = dp[i][j]+1
                    dp[i+1][j|(1<<(i+1))] = dp[i][j]+1

ans = 0
for i in range(10):
    ans += dp[i][-1]

pprint(dp, width=10000)
print(ans%(10**9))
