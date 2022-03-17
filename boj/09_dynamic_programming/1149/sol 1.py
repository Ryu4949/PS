'''
뭔가 RGB의 최대값과 최소값의 차이가 가장 큰 곳부터 지정해줘야될듯: 아님
2차원 리스트로 해야되나? 맞는듯??
'''

N = int(input())
RGB = []
for _ in range(N):
    RGB.append(list(map(int, input().split())))

#dp[i][j]는 i번째 집에 j번째 색을 칠할 때의 최소비용
#그래서 j가 만약 0이라면 i-1번째 집의 최소비용중 1번째 색이나 2번째 색을 칠한 경우의 최소비용을 고려해야함(색이 겹치면 안되니까)
dp = [[0] * 3 for _ in range(N)]
for i in range(3):
    dp[0][i] = RGB[0][i]

for i in range(1, N):
    for j in range(3):
        dp[i][j] = min(RGB[i][j]+dp[i-1][(j+1)%3], RGB[i][j]+dp[i-1][(j+2)%3])

print(min(dp[-1]))