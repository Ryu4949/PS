N = int(input())
dp = [4] * 50001

r = int(N ** (1/2)) + 1
dp[0] = 0
dp[1] = 1
for i in range(2, N+1):
    j = 1
    while j**2 <= i:
        dp[i] = min(dp[i], dp[i-j**2]+1)
        j += 1

print(dp[N])
