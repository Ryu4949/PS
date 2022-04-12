N = int(input())
boxes = [*map(int, input().split())]
dp = [1] * N

for i in range(N-1):
    for j in range(i+1, N):
        if boxes[j] > boxes[i]:
            dp[j] = max(dp[j], dp[i]+1)

print(max(dp))