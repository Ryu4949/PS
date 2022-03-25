T= int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())

    board = [[[[0, -5, 0] for _ in range(N)]for _ in range(N)] for _ in range(2)]
    cur = 0
    next = 1

    for _ in range(K):
        a, b, c, d = map(int, input().split())
        board[cur][a][b][0] = c
        if d == 1 or d == 4:
            board[cur][a][b][1] = d-1
        else:
            board[cur][a][b][1] = 4-d

    dr = [-1, 0, 1, 0]
    dc = [0, -1, 0, 1]

    def move(r, c, d):
        if d == -5:
            return
        rr, cc = r+dr[d], c+dc[d]

        if rr == 0 or rr == N-1 or cc == 0 or cc == N-1:
            board[next][rr][cc][0] = board[cur][r][c][0] // 2
            if board[next][rr][cc][0] != 0:
                board[next][rr][cc][1] = (board[cur][r][c][1]+2) % 4
            else:
                board[next][rr][cc][1] = -5
            board[cur][r][c] = [0, -5, 0]
        else:
            board[next][rr][cc][2] = max(board[next][rr][cc][2], board[cur][r][c][0])
            if board[cur][r][c][0] >= board[next][rr][cc][2]:
                board[next][rr][cc][1] = board[cur][r][c][1]
            board[next][rr][cc][0] += board[cur][r][c][0]
            board[cur][r][c] = [0, -5, 0]

    for t in range(1, M+1):
        for i in range(N):
            for j in range(N):
                move(i, j, board[cur][i][j][1])
        cur, next = next, cur


    ans = 0
    for i in range(N):
        for j in range(N):
            ans += board[cur][i][j][0]
    print(f'#{tc} {ans}')