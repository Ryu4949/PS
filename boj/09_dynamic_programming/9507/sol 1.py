def koong(n):
    dp = [0] * 68
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    if n <= 3:
        return dp[n]

    for i in range(4, 68):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3] + dp[i-4]

    return dp[n]

t = int(input())
for _ in range(t):
    num = int(input())
    print(koong(num))
