T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(input()) for _ in range(N)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    def dfs(row, col):
        if 0<=row<N and 0<=col<N and maze[row][col] != '1':
            maze[row][col] = '1'
            for i in range(4):
                rr, cc = row+dr[i], col+dc[i]
                dfs(rr, cc)

    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                r, c = i, j
                break

    for i in range(N):
        for j in range(N):
            if maze[i][j] == '3':
                x, y = i, j
                break

    dfs(r, c)

    if maze[x][y] == '1':
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')