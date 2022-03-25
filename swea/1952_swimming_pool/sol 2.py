T = int(input())
for tc in range(1, T+1):
    price = list(map(int, input().split()))
    plan = [0] + list(map(int, input().split()))
    N = 12

    month = [0, 1, 3, 12]
    dp = [0] * 13

    for i in range(1, N+1):
        dp[i] = min(dp[i-1]+plan[i] * price[0], dp[i-1]+price[1], dp[max(i-3, 0)]+price[2], dp[0] + price[3])

    print(dp[N])

