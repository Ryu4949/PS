#메모리초과?

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1] * N for _ in range(M)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c):
    if r == 0 and c == 0:
        return 1

    if dp[r][c] == -1:
        dp[r][c] = 0

        for i in range(4):
            rr, cc = r+dr[i], c+dc[i]
            if 0 <=rr<M and 0<=cc<N and graph[rr][cc] > graph[r][c]:
                dp[r][c] += dfs(rr, cc)

    return dp[r][c]

print(dfs(M-1, N-1))