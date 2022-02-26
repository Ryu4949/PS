def dfs(r, c):
    global cnt
    stack = [(r, c)]
    visited[r][c] = True

    while stack:
        r, c = stack.pop()

        for i in range(4):
            rr, cc = r+dr[i], c+dc[i]
            if 0<=rr<N and 0<=cc<M and not visited[rr][cc] and campus[rr][cc] == 'O':
                visited[rr][cc] = True
                stack.append((rr, cc))
            elif 0<=rr<N and 0<=cc<M and not visited[rr][cc] and campus[rr][cc] == 'P':
                cnt += 1
                visited[rr][cc] = True
                stack.append((rr, cc))

N, M = map(int, input().split())
campus = [list(input()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]


for i in range(N):
    for j in range(M):
        if campus[i][j] == 'I':
            sx, sy = i, j

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

cnt = 0

dfs(sx, sy)

if cnt >= 1:
    print(cnt)
else:
    print('TT')