from pprint import pprint

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

    pprint(board[cur], width = 100)
    dr = [-1, 0, 1, 0]
    dc = [0, -1, 0, 1]

    def move(r, c, d):
        if d == -5:
            return
        rr, cc = r+dr[d], c+dc[d]

        #다음 위치가 약이 칠해져있는 위치라면
        if rr == 0 or rr == N-1 or cc == 0 or cc == N-1:
            #다음 위치의 미생물 수는 현재 위치의 절반이 됨
            board[next][rr][cc][0] = board[cur][r][c][0] // 2
            #절반을 한 값이 0이 아니라면
            if board[next][rr][cc][0] != 0:
                #이동 방향은 현재의 반대
                board[next][rr][cc][1] = (board[cur][r][c][1]+2) % 4
            #0이 돼버리면
            else:
                #이동 방향 값 초기화
                board[next][rr][cc][1] = -5
            #현재 위치 초기화
            board[cur][r][c] = [0, -5, 0]
        #다음 위치가 약이 칠해진 곳이 아니라면
        else:
            #다음 위치에 더해진 미생물 수 중 가장 큰 값을 2번째 index에 저장하고
            board[next][rr][cc][2] = max(board[next][rr][cc][2], board[cur][r][c][0])
            #만약 이번에 더해질 미생물 수가, 이동할 위치에 이미 더해진 값들 중 최대값보다 크거나 같으면
            if board[cur][r][c][0] >= board[next][rr][cc][2]:
                #이동방향을 이번에 더할 미생물 군집의 이동방향으로 바꾸기
                board[next][rr][cc][1] = board[cur][r][c][1]
            #다음 위치에 현재 미생물 수 더하기
            board[next][rr][cc][0] += board[cur][r][c][0]
            #현재 위치 초기화
            board[cur][r][c] = [0, -5, 0]

    for t in range(1, M+1):
        for i in range(N):
            for j in range(N):
                move(i, j, board[cur][i][j][1])
        print(f'{t}시간 경과')
        pprint(board[next], width = 100)
        cur, next = next, cur


    ans = 0
    for i in range(N):
        for j in range(N):
            ans += board[cur][i][j][0]
    print(f'#{tc} {ans}')