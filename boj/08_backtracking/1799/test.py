import sys
from pprint import pprint
input = sys.stdin.readline


N = int(input())
chess = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
board = [[0] * N for _ in range(N)]
cnt = 0
ans = -float('inf')

#체스판 0인 곳은 먼저 방문처리
for i in range(N):
    for j in range(N):
        if chess[i][j] == 0:
            visited[i][j] = True

dr = [-1, -1, 1, 1]
dc = [-1, 1, 1, -1]

#(r, c)에 비숍을 놓았을 때 그 대각선 방향으로 방문처리 해주는 함수
def check(r, c):
    for i in range(4):
        p = 0
        while True:
            rr, cc = r+dr[i]*p, c+dc[i]*p
            if 0<=rr<N and 0<=cc<N:
                visited[rr][cc] = True
                p += 1
            else:
                break

def dfs(i):
    global cnt, ans

    if i == N:
        ans = max(ans, cnt)
        return

    for j in range(N):
        if chess[i][j] == 1 and not visited[i][j]:
            dfs(i+1)
            check(i, j)
            cnt += 1
            dfs(i+1)
check(2, 2)
check(4, 2)
pprint(visited)
