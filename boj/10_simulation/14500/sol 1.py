def dfs(r, c, i, val):  #나머지 블럭 처리
    if i == 4:
        rlt.append(val)
        return

    for j in range(4):
        rr, cc = r+dr[j], c+dc[j]

        if 0<=rr<N and 0<=cc<M and not visited[rr][cc]:
            visited[rr][cc] = True
            dfs(rr, cc, i+1, val+board[r][c])
            visited[rr][cc] = False

def t_block(r, c):  #t-블럭 처리
    val = board[r][c]
    v = [0] * 4

    for i in range(4):
        rr, cc = r+dr[i], c+dc[i]

        if 0<=rr<N and 0<=cc<M:
            v[i] = board[rr][cc]

    val += sum(v)
    val -= min(v)

    rlt.append(val)

N, M = map(int, input().split())
board = [[*map(int, input().split())] for _ in range(N)]
visited = [[False] * M for _ in range(N)]
rlt = []

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, 0, 0)
        visited[i][j] = False
        t_block(i, j)

print(max(rlt))
