def dfs(i):
    global sum_height, ans
    if i == N:
        if sum_height >= B:
            ans = min(ans, (sum_height - B))
        return

    dfs(i + 1)
    sum_height += heights[i]
    dfs(i + 1)
    sum_height -= heights[i]

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    sum_height = 0
    ans = float('inf')

    dfs(0)
    print(f'#{tc} {ans}')