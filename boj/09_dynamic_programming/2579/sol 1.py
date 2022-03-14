N = int(input())
score = [0]
for _ in range(N):
    score.append(int(input()))

dp = [0] * (N+1)

def stairs(N):
    #계단 1~2개면 둘다 밟기
    if N == 1:
        return(score[N])
    elif N == 2:
        return score[1] + score[2]
    # 계단 3개면 1,3 2,3중 점수 높은 쪽으로 밟기
    elif N==3:
        return max(score[1]+score[3], score[2]+score[3])
    else:
        dp[1] = score[1]
        dp[2] = score[1]+score[2]
        dp[3] = max(score[1]+score[3], score[2]+score[3])

        #4개부터는 2칸 밑의 계단을 밟았는지 여부로 나눠서
        #i-2 계단을 안밟았으면 dp[i-3]에 끝 2개의 계단 점수의 합
        #밟았으면 다음계단을 안밟아야 마지막 계단을 밟을 수 있으니까 dp[i-2] + 마지막 계단 점수
        for i in range(4, N+1):
            dp[i] = max(dp[i-3]+score[i-1]+score[i], dp[i-2]+score[i])
        return dp[N]

print(stairs(N))
