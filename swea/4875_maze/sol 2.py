T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(input()) for _ in range(N)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    stack = []
    def dfs(row, col):  #출발점의 좌표를 받아서
        stack.append((row, col))    #스택에 넣고
        maze[row][col] = '1'    #출발점을 1로 바꿔주기

        while stack:    #스택이 빌 때까지
            r, c = stack.pop()  #스택에서 하나를 pop해서 행/열의 인덱스를 r과 c로 놓고
            for i in range(4):  #상하좌우 탐색
                rr, cc = r+dr[i], c+dc[i]   
                if 0<=rr<N and 0<=cc<N and maze[rr][cc] != '1': #상하좌우가 범위 내에 있고, 이미 방문한 곳이나 벽이 아니라면
                    stack.append((rr, cc))  #해당 좌표를 스택에 push하고
                    maze[rr][cc] = '1'  #방문처리

    #출발점 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                r, c = i, j
                break
    #목표지점 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '3':
                x, y = i, j
                break
    #dfs 시행
    dfs(r, c)

    #도착점의 값이 1이면 1, 여전히 3이면 0 출력
    if maze[x][y] == '1':
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')