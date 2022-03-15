T = int(input())
for _ in range(T):
    N = int(input())
    dp = [0] * 1000001
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for i in range(4, N+1):
        dp[i] = (dp[i - 3] + dp[i - 2] + dp[i - 1]) % 1000000009
    print(dp[N])
