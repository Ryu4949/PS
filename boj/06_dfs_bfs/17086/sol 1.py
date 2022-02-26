from collections import deque

dr = [-1, 1, 0, 0, -1, -1, 1, 1]
dc = [0, 0, -1, 1, -1, 1, 1, -1]

#r, c는 위치좌표고 s는 이동한 거리를 담을 변수
def bfs(r, c, s):
    visited = [[-1] * M for _ in range(N)]
    queue = deque([(r, c, s)])
    #시작점을 0으로 방문처리
    visited[r][c] = 0

    #만약 시작점이 상어가 있는 자리라면 0 반환
    if shark[r][c] == '1':
        return 0

    while queue:
        r, c, s = queue.popleft()

        for i in range(8):
            rr, cc = r+dr[i], c+dc[i]
            #rr, cc가 범위 내이고, 아직 방문하지 않은 경우
            if 0<=rr<N and 0<=cc<M and visited[rr][cc] == -1:
                #만약 rr, cc 위치가 빈칸이면 계속 이동
                if shark[rr][cc] == '0':
                    queue.append((rr, cc, s+1))
                    visited[rr][cc] = visited[r][c] + 1
                #만약 rr, cc 위치에 상어가 있다면, 현재까지 이동한 거리에 1을 더해서 리턴
                elif shark[rr][cc] == '1':
                    return s+1

N, M = map(int, input().split())
shark = [list(input().split()) for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(M):
        ans = max(ans, bfs(i, j, 0))

print(ans)