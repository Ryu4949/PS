from collections import deque
R, C = map(int, input().split())
field = [list(input()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c):
    wolves = 0
    sheep = 0
    queue = deque([(r, c)])
    visited[r][c] = True
    if visited[r][c] == 'v':
        wolves += 1
    elif visited[r][c] == 'o':
        sheep += 1

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            rr, cc = r+dr[i], c+dc[i]

            if 0<=rr<R and 0<=cc<C and not visited[rr][cc] and field[rr][cc] != '#':
                if field[rr][cc] == 'v':
                    wolves += 1
                elif field[rr][cc] == 'o':
                    sheep += 1

                visited[rr][cc] = True
                queue.append((rr, cc))
    print(f'조정 전 wolves: {wolves}, sheep: {sheep}')
    if wolves >= sheep:
        sheep = 0
    else:
        wolves = 0

    return (sheep, wolves)

cnt = [0, 0]
for i in range(R):
    for j in range(C):
        if not visited[i][j] and field[i][j] != '#':
            rlt = bfs(i, j)
            print(f'i, j: {i, j}, sheep, wolves: {rlt[0], rlt[1]}')
            cnt[0] += rlt[0]
            cnt[1] += rlt[1]

print(*cnt)