for _ in range(10):
    T = int(input())
    maze = [list(input()) for _ in range(16)]
    visited = [[False] * 16 for _ in range(16)]
    for i in range(16):
        for j in range(16):
            #출발점 찾기
            if maze[i][j] == '2':
                sx = i
                sy = j

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    def dfs(r, c):
        #스택에 넣고 방문처리
        stack = [(r,c)]
        visited[r][c] = True

        while stack:
            r, c = stack.pop()

            for i in range(4):
                rr, cc = r+dr[i], c+dc[i]

                #다음 위치가 범위 내이고, 벽이 아니면서 아직 방문하지 않았다면
                if 0<=rr<16 and 0<=cc<16 and not visited[rr][cc] and maze[rr][cc] != '1':
                    #해당 위치 스택에 넣고 방문처리
                    stack.append((rr, cc))
                    visited[rr][cc] = True

                    #다음위치가 방문가능하면서 도착점이면 1반환
                    if maze[rr][cc] == '3':
                        return 1

        #탐색을 마칠동안 도착점에 도달하지 못한 경우이므로 0 반환
        return 0

    print(f'#{T} {dfs(sx, sy)}')