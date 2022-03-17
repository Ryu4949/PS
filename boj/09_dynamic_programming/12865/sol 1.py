'''
(무게, 가치)를 하나씩 고려하면서
최대값을 갱신할 때
현재 위치에서 현재의 물건을 넣을 때와 넣지 않을 때 최대값을 비교하려면
현재 위치의 dp값과, 현재 위치에서 지금 넣으려는 물건의 무게를 뺀 위치의 dp값에다가 가치.. ㅅㅂ 무슨말이야
를 넣을 떄의 값을 비교해서 최대값으로
'''

from pprint import pprint

N, K = map(int, input().split())
W = [0]
V = [0]
for _ in range(N):
    w, v = map(int, input().split())
    W.append(w)
    V.append(v)
dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        w = W[i]
        v = V[i]

        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)

print(dp[-1][-1])