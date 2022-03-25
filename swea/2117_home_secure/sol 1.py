from collections import deque
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    def bfs(r, c):
        visited = [[False] * N for _ in range(N)]
        queue = deque([(r, c, 1)])
        cnt = [[0, 0] for _ in range(N+2)]
        visited[r][c] = True
        if graph[r][c] == 1:
            cnt[1][0] += M
            cnt[1][1] += 1

        while queue:
            r, c, d = queue.popleft()
            if d == N+1:
                break

            for i in range(4):
                rr, cc = r+dr[i], c+dc[i]

                if 0<=rr<N and 0<=cc<N and not visited[rr][cc]:
                    if graph[rr][cc] == 1:
                        cnt[d+1][0] += M
                        cnt[d+1][1] += 1
                        queue.append((rr, cc, d+1))
                        visited[rr][cc] = True
                    else:
                        queue.append((rr, cc, d+1))
                        visited[rr][cc] = True

        dp = [[0, 0] for _ in range(N+2)]
        for i in range(1, N+2):
            dp[i][1] = dp[i-1][1] + cnt[i][1]
            dp[i][0] = dp[i-1][0] + cnt[i][0]
        for i in range(1, N+2):
            dp[i][0] -= i**2 + (i-1)**2

        homes = 0
        for i in range(1, N+2):
            if dp[i][0] > 0:
                homes = max(homes, dp[i][1])
        return homes

    ans = 0
    for i in range(N):
        for j in range(N):
            ans = max(ans, bfs(i, j))
    print(f'#{tc} {ans}')
