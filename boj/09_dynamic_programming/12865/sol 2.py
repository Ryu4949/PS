#시간초과

N, K = map(int, input().split())
W = []
V = []
for _ in range(N):
    w, v = map(int, input().split())
    W.append(w)
    V.append(v)

ans = 0
sum_value = 0
sum_weight = 0

def dfs(i):
    global ans, sum_value, sum_weight
    if sum_weight > K:
        return

    if i == N:
        ans = max(ans, sum_value)
        return

    sum_weight += W[i]
    sum_value += V[i]
    dfs(i+1)
    sum_weight -= W[i]
    sum_value -= V[i]
    dfs(i+1)

dfs(0)

print(ans)