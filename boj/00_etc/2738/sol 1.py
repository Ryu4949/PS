N, M = map(int, input().split())
ans = [[0]*M for _ in range(N)]

for _ in range(2):
    for i in range(N):
        nums = [*map(int, input().split())]
        for j in range(M):
            ans[i][j] += nums[j]

for r in range(N):
    print(*ans[r])