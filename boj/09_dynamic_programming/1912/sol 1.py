'''
dp[i] : i번째까지 더했을 때 최대 합
dp[i-1]이 음수면 더해줄 이유가 없기 때문에 arr[i]가 되고,
dp[i-1]이 양수면 dp[i] = dp[i-1] + arr[i]가 됨
'''

N = int(input())
arr = list(map(int, input().split()))
dp = [0] * N

dp[0] = arr[0]
for i in range(1, N):
    dp[i] = dp[i-1] + arr[i] if dp[i-1] >= 0 else arr[i]

print(max(dp))