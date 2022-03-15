T= int(input())
for _ in range(T):
    N = int(input())
    dp = [0] * (N+1)

    def plus(N):
        if N <= 2:
            return N
        elif N == 3:
            return 4
        else:
            dp[1] = 1
            dp[2] = 2
            dp[3] = 4

            #예를 들어 5를 만드려면 4에다가 1, 3에다가 2, 2에다가 3 더하면 됨
            #3에다가 1+1 하는건 4에다가 1에 포함됨
            for i in range(4, N+1):
                dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
            return dp[N]

    print(plus(N))
