T = int(input())
for tc in range(1, T+1):
    price = list(map(int, input().split()))
    plan = [0] + list(map(int, input().split()))
    N = 12

    month = [0, 1, 3, 12]
    dp = [0] * 13

    for i in range(1, N+1):
        #순서대로 지난달의 비용에 이번달을 1일권 쓸경우, 저번달 비용에 한달권 쓸경우,
        #세달전 비용(3월 이전이면 1월 비용)에 3개월권 쓸 경우, 12개월 전 비용에 1년권 쓸경우 중에서 최소값으로 갱신
        dp[i] = min(dp[i-1]+plan[i] * price[0], dp[i-1]+price[1], dp[max(i-3, 0)]+price[2], dp[0] + price[3])

    print(dp[N])

