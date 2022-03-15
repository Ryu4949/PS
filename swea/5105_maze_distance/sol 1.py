from collections import deque

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(input()) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]

    #출발점 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                sx = i
                sy = j

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    def bfs(r, c):
        #큐에 위치정보와 거리정보 같이 담고 방문처리
        queue = deque([(r, c, 0)])
        visited[r][c] = True

        while queue:
            r, c, d = queue.popleft()

            for i in range(4):
                rr, cc = r+dr[i], c+dc[i]

                #다음 위치가 범위 내이고 방문하지 않았으면서 벽이 아니면
                if 0<=rr<N and 0<=cc<N and not visited[rr][cc] and maze[rr][cc] != '1':
                    #다음 위치와 거리 +1 해서 큐에 추가, 방문처리
                    queue.append((rr, cc, d+1))
                    visited[rr][cc] = True

                    #만약 다음 위치가 도착점이라면 현재까지 지나온 칸 수를 반환
                    if maze[rr][cc] == '3':
                        return d
        #탐색을 마칠동안 도착점에 도달하지 못했다면 0 반환환
        return 0

    print(f'#{tc} {bfs(sx, sy)}')