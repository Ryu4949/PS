from collections import deque

def bfs(x, y):
    cnt = 1
    queue = deque([(x, y)])
    visited[room[x][y]] = True

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            rr, cc = r+dr[i], c+dc[i]
            if 0<=rr<N and 0<=cc<N and room[rr][cc] == room[r][c] + 1:
                cnt += 1
                queue.append((rr, cc))
                visited[room[rr][cc]] = True

    rlt.append((cnt, room[x][y]))

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    room = []
    for _ in range(N):
        room.append(list(map(int, input().split())))
    visited = [False] * (N**2+1)
    rlt = []

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for i in range(N):
        for j in range(N):
            if not visited[room[i][j]]:
                bfs(i, j)
    rlt.sort(key = lambda x: (-x[0], x[1]))

    print(f'#{tc} {rlt[0][1]} {rlt[0][0]}')