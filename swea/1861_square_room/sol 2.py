#시간초과

from collections import deque

def bfs(r, c):
    if visited[r][c] != -1:
        return

    queue = deque([(r, c)])
    visited[r][c] = 1

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            rr, cc = r+dr[i], c+dc[i]
            if 0<=rr<N and 0<=cc<N and visited[rr][cc]==-1 and room[rr][cc] == room[r][c] + 1:
                visited[rr][cc] = visited[r][c] + 1
                queue.append((rr, cc))


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    room = []
    for _ in range(N):
        room.append(list(map(int, input().split())))

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    visited = [[-1] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            bfs(i, j)

    print(f'#{tc} {start} {ans}')