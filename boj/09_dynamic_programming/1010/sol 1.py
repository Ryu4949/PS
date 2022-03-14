T = int(input())
dp = [0] * 31

def factorial(N):
    dp[0] = 1

    for i in range(1, N + 1):
        dp[i] = dp[i - 1] * i

factorial(30)

for _ in range(T):
    N, M = map(int, input().split())
    print(dp[M] // dp[N] // dp[M-N])