N = int(input())
dp = [0] * 1001

dp[1] = 'SK'
dp[3] = 'SK'

for i in range(2, N+1):
    if dp[i] == 0:
        if dp[i-1] == 'SK' or dp[i-3] == 'SK':
            dp[i] = 'CY'
        else:
            dp[i] = 'SK'

print(dp[N])