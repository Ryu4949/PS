N = int(input())
soldiers = [*map(int, input().split())]
dp = [1] * N

for i in range(N-1, 0, -1):
    for j in range(i-1, -1, -1):
        if soldiers[j] > soldiers[i]:
            dp[j] = max(dp[j], dp[i]+1)

print(N-max(dp))

