def check(t):
    limit = K
    for i in range(N):
        if limit >= 0 and X[i] >= t:
            return True
        elif limit >= 0 and X[i] < t:
            limit -= t-X[i]
        else:
            return False

N, K = map(int, input().split())
X = []
for _ in range(N):
    X.append(int(input()))
X.sort()

start = min(X)
end = max(X) + K

ans = 0
while start <= end:
    mid = (start + end) // 2
    if check(mid):
        ans = mid
        start = mid + 1
    else:
        end = mid - 1

print(ans)