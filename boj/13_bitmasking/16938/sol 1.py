N, L, R, X = map(int, input().split())
A = [*map(int, input().split())]
A.sort()

ans = 0
for i in range(1<<N):
    total = 0
    cnt = 0
    easy = max(A)+1
    hard = 0
    for j in range(N):
        if i & (1<<j):
            cnt += 1
            total += A[j]
            easy = min(easy, A[j])
            hard = max(hard, A[j])

    if cnt>=2 and L<=total<=R and hard-easy>=X:
        ans += 1

print(ans)