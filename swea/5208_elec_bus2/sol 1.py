T= int(input())
for tc in range(1, T+1):
    charge = list(map(int, input().split()))
    N = charge[0]
    dp = [N] * (N+1)    #초기값은 충전 횟수로 불가능한 큰 수 중 아무거나
    dp[0] = 0
    for i in range(1, charge[1]+2): #초기값은 1번 정류장에서 충전한 상태로 갈 수 있는 곳까지는 0으로
        dp[i] = 0

    for i in range(2, N):   #2번 정류장부터
        for j in range(i+1, i+charge[i]+1): #해당 정류장에서 충전했을 때 갈 수 있는 정류장까지 확인
            if j <= N:
                dp[j] = min(dp[j], dp[i]+1) #기존에 저장된 값과, i번 정류장에 도달할 수 있는 최소 충전횟수 + 1을 비교

    print(f'#{tc} {dp[-1]}')