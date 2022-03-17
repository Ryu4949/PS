'''
- 행이 2개니까, 같은 행의 스티커를 연속해서 두개를 뗄 수는 없고
- 행을 달리하면 연속한 열의 스티커를 뗄 수 있다
- 예시문제처럼 한 행에 5개의 스티커가 있을 때, 무조건 5개를 떼는 게 점수를 최대로 하는 방법일까?
- 그렇지 않다 예시문제에서 3번째 열(인덱스로 치면 2번째)에서 100을 뗴고, 다음 열에서 아래 행의 10을 떼고, 다시 마지막 행의 40을 떼는 경우와
- 3열에서 100을 떼고, 그 다음 열은 둘다 떼지 않고 마지막 열에서 60을 떼는 경우 뗀 스티커의 수는 하나 적지만 점수는 오히려 높다
- dp테이블을 2차원 리스트로 하면 좋을 것 같다. RGB 문제처럼
- dp[i][j]는 sticker[i][j]를 뗄 경우에 얻을 수 있는 점수의 최댓값
'''

T = int(input())
for _ in range(T):
    N = int(input())
    sticker = [[] for _ in range(N)]
    for _ in range(2):
        st = list(map(int, input().split()))
        for i in range(N):
            sticker[i].append(st[i])

    dp = [[0] * 2 for _ in range(N)]
    dp[0] = sticker[0]
    if N >= 2:
        dp[1][0] = dp[0][1] + sticker[1][0]
        dp[1][1] = dp[0][0] + sticker[1][1]
    if N >= 3:
        for i in range(2, N):
            for j in range(2):
                dp[i][j] = max(dp[i-1][1-j]+sticker[i][j], dp[i-2][1-j]+sticker[i][j])

    print(max(dp[-1]))