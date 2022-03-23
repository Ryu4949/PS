#현재 위치 (r, c)에서 방향이 정해졌을 때 그 위치로 돌을 뒤집을 수 있는지 확인하는 함수
from pprint import pprint

def othello(r, c, d):
    p = 1
    change = []
    while True:
        rr, cc = r+dr[d]*p, c+dc[d]*p

        #범위 내이면서 놓은 돌의 색과 다른 색을 만나면 change에 추가하고 한칸 더 진행하기 위해 p += 1
        if 0<=rr<N and 0<=cc<N and board[r][c] + board[rr][cc] == 3:
            p += 1
            change.append((rr, cc))
        #범위 내인데 같은 색을 만나면 거기서 반복 중단
        elif 0<=rr<N and 0<=cc<N and board[r][c] == board[rr][cc]:
            break
        #다시 자신과 같은 색을 만나기 전에 범위를 벗어나거나, 범위 내이지만 빈칸을 만나는 경우
        #이때는 돌을 뒤집을 수 없으므로 change를 초기화하고 중단
        else:
            change = []
            break
    #change에 있는 위치의 돌들을 뒤집기
    for rr, cc in change:
        board[rr][cc] = 3 - board[rr][cc]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = [[0] * N for _ in range(N)]
    board[N//2-1][N//2-1], board[N//2][N//2], board[N//2-1][N//2], board[N//2][N//2-1] = 2, 2, 1, 1

    pprint(board)
    #상하좌우 / 왼쪽 위부터 시계방향 대각선
    dr = [-1, 1, 0, 0, -1, -1, 1, 1]
    dc = [0, 0, -1, 1, -1, 1, 1, -1]

    pprint(board, width = 20)
    for _ in range(M):
        a, b, c = map(int, input().split())
        #돌을 놓고
        board[b-1][a-1] = c
        #8방향 체크
        for i in range(8):
            othello(b-1, a-1, i)

    black = 0
    white = 0

    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                black += 1
            if board[i][j] == 2:
                white += 1

    print(f'#{tc} {black} {white}')
