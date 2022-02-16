for _ in range(10):
    n = int(input())
    #도착점이 2이므로 도착점으로부터 역으로 이동
    board = []
    for _ in range(100):
        board.append(list(map(int, input().split())))
    #위(0), 왼쪽(1), 오른쪽(2)
    dx = [-1, 0, 0]
    dy = [0, -1, 1]
    move = 0

    x = 99
    #마지막 줄에서 도착지점이 있는 위치 찾기
    for i in range(100):
        if board[99][i] == 2:
            y = i
            break

    while True:
        #위로 이동 중일 때
        if move == 0:
            #범위 내이고 왼쪽에 막대기가 있으면 방향을 왼쪽으로 전환
            if y-1 >= 0 and board[x][y-1] == 1:
                move = 1
            #범위 내이고 오른쪽에 막대기가 있으면 방향을 오른쪽으로 전환
            elif y+1 <= 99 and board[x][y+1] == 1:
                move = 2
        #왼쪽으로 이동 중 세로 방향의 막대기를 만나면 위로 방향 전환
        elif move == 1:
            if board[x-1][y] == 1:
                move = 0
        #오른쪽으로 이동 중 세로 방향의 막대기를 만나면 위로 방향 전환
        else:
            if board[x-1][y] == 1:
                move = 0

        x += dx[move]
        y += dy[move]
        #첫줄에 도달하면 종료
        if x == 0:
            break
    #종료시점에서 위치를 출력
    print(f'#{n} {y}')