T = int(input())
for tc in range(1, T+1):
    price = [0] + list(map(int, input().split()))
    plan = [0] + list(map(int, input().split()))

    month = [0, 0, 1, 3, 12]
    dp = [[0] * len(plan) for _ in range(len(price))]

    for i in range(1, len(plan)):
        dp[1][i] = dp[1][i-1] + price[1] * plan[i]

    # print(dp[1])
    #dp[i][j]: i번째 이용권까지 고려할 때, j번쨰 달을 이용하는 최소금액
    for i in range(2, len(price)):
        for j in range(1, len(plan)):
            dp[i][j] = min(dp[i][j-1]+dp[i-1][j]-dp[i-1][j-1], dp[i][max(j-day[i], 0)]+price[i])
        # print(dp[i])
    print(f'#{tc} {dp[-1][-1]}')