N = int(input())
T = [0]
P = [0]
for _ in range(N):
    a, b = map(int, input().split())
    T.append(a)
    P.append(b)

dp = [0] * (N+1)

if T[-1] == 1:
    dp[-1] = P[-1]

for i in range(N-1, 0, -1):
    if i+T[i]-1 <= N:
        if i+T[i] == N+1:
            dp[i] = max(dp[i+1], P[i])
        else:
            dp[i] = max(dp[i+1], dp[i+T[i]]+P[i])
    else:
        dp[i] = dp[i+1]

print(dp[1])