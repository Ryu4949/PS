N = int(input())
dp = [0] * 1001

dp[1] = 'CY'

for i in range(2, N+1):
    if dp[i] == 0:
        if dp[i-1] == 'CY' or dp[i-3] == 'CY' or dp[i-4] == 'CY':
            dp[i] = 'SK'
        else:
            dp[i] = 'CY'

print(dp[N])