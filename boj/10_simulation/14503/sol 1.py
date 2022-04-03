N, M = map(int, input().split())
sx, sy, d = map(int, input().split())
room = [[*map(int, input().split())] for _ in range(N)]
visited = [[-1] * M for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

visited[sx][sy] = 2
stack = [(sx, sy, d, 0)]

while True:
    r, c, d, s = stack.pop()

    if s == 4:
        if room[r+dr[(d+2)%4]][c+dc[(d+2)%4]] == 1:
            break
        else:
            stack.append((r+dr[(d+2)%4], c+dc[(d+2)%4], d, 0))
            continue

    dd = (d-1)%4
    ss = s+1
    rr, cc = r+dr[dd], c+dc[dd]

    if 0<=rr<N and 0<=cc<M and visited[rr][cc] == -1 and room[rr][cc] == 0:
        visited[rr][cc] = 2
        stack.append((rr, cc, dd, 0))
    else:
        stack.append((r, c, dd, ss))

ans = 0
for i in range(N):
    for j in range(M):
        if visited[i][j] == 2:
            ans += 1

print(ans)