#시간초과

from collections import deque

def bfs(r, c):
    visited = [[False]* N for _ in range(N)]
    cnt = 1
    queue = deque([(r, c)])
    visited[r][c] = True

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            rr, cc = r+dr[i], c+dc[i]
            if 0<=rr<N and 0<=cc<N and not visited[rr][cc] and room[rr][cc] == room[r][c] + 1:
                visited[rr][cc] = True
                cnt += 1
                queue.append((rr, cc))

    return cnt

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    room = []
    for _ in range(N):
        room.append(list(map(int, input().split())))

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    start = 0
    ans = 0
    for i in range(N):
        for j in range(N):
            move = bfs(i, j)
            if move > ans:
                ans = move
                start = room[i][j]
            if move == ans:
                start = min(start, room[i][j])

    print(f'#{tc} {start} {ans}')