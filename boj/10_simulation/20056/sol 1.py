def move(r, c):
    if graph[r][c][0][0] == 0:
        return

    if graph[r][c][0][2] == 'even':
        s = graph[r][c][0][1]
        for i in [0, 2, 4, 6]:
            rr, cc = (r+dr[i]*s)%N, (c+dc[i]*s)%N
            graph[rr][cc][1][0] += graph[r][c][0][0] // 4
            graph[rr][cc][1][1] += graph[r][c][0][1]
            graph[rr][cc][1][2] += i % 2
            graph[rr][cc][1][3] += 1
            graph[rr][cc][1][4] += i

    elif graph[r][c][0][2] == 'odd':
        s = graph[r][c][0][1]
        for i in [1, 3, 5, 7]:
            rr, cc = (r+dr[i]*s)%N, (c+dc[i]*s)%N
            graph[rr][cc][1][0] += graph[r][c][0][0] // 4
            graph[rr][cc][1][1] += graph[r][c][0][1]
            graph[rr][cc][1][2] += i % 2
            graph[rr][cc][1][3] += 1
            graph[rr][cc][1][4] += i

    else:
        s = graph[r][c][0][1]
        d = graph[r][c][0][2]
        rr, cc = (r+dr[d]*s)%N, (c+dc[d]*s)%N
        graph[rr][cc][1][0] += graph[r][c][0][0]
        graph[rr][cc][1][1] += graph[r][c][0][1]
        graph[rr][cc][1][2] += graph[r][c][0][2] % 2
        graph[rr][cc][1][3] += 1
        graph[rr][cc][1][4] += graph[r][c][0][2]

    for i in range(5):
        graph[r][c][0][i] = 0

def adjust(r, c):
    if graph[r][c][1][3] >= 2:
        if graph[r][c][1][0] < 5:
            for i in range(5):
                graph[r][c][0][i] = 0
                graph[r][c][1][i] = 0
        else:
            graph[r][c][0][0] = (graph[r][c][1][0]//5)*4
            graph[r][c][0][1] = graph[r][c][1][1]//graph[r][c][1][3]
            if graph[r][c][1][2] == 0 or graph[r][c][1][2] == graph[r][c][1][3]:
                graph[r][c][0][2] = 'even'
            else:
                graph[r][c][0][2] = 'odd'

    elif graph[r][c][1][3] == 1:
        for i in range(2):
            graph[r][c][0][i] = graph[r][c][1][i]
        graph[r][c][0][2] = graph[r][c][1][4]

    for i in range(5):
        graph[r][c][1][i] = 0

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

N, M, K = map(int, input().split())
graph = [[[[0] * 5 for _ in range(2)] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    a, b, c, d, e = map(int, input().split())
    graph[a-1][b-1][0][0] = c
    graph[a-1][b-1][0][1] = d
    graph[a-1][b-1][0][2] = e
    graph[a-1][b-1][0][4] = e

cnt = 0
while True:
    cnt += 1

    for i in range(N):
        for j in range(N):
            move(i, j)

    for i in range(N):
        for j in range(N):
            adjust(i, j)

    if cnt == K:
        break

ans = 0
for i in range(N):
    for j in range(N):
        ans += graph[i][j][0][0]

print(ans)