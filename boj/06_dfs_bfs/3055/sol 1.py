import sys
from collections import deque
input = sys.stdin.readline

#bfs
def bfs(r, c):
    queue = deque([(r, c)])
    visited[r][c] = True
    graph[r][c] = 0

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            rr, cc = r+dr[i], c+dc[i]

            if 0<=rr<R and 0<=cc<C and not visited[rr][cc]:
                #다음 위치가 방문하지 않은 빈 곳이라면
                if forest[rr][cc] == '.':
                    #방문처리하고, 그곳까지 물이 도달하는 최단 시간 갱신
                    visited[rr][cc] = True
                    graph[rr][cc] = min(graph[rr][cc], graph[r][c] + 1)
                    queue.append((rr, cc))


R, C = map(int, input().split())
#forest는 입력데이터, graph는 물이 도달하는 시간 기록과 고슴도치가 이동하는 시간
forest = [list(input()) for _ in range(R)]
graph = [[float('inf')] * C for _ in range(R)]

#water에는 물이차있는 지역의 좌표를 담고, start와 goal은 각각 고슴도치의 출발위치와 비버굴의 위치
water = []
for i in range(R):
    for j in range(C):
        if forest[i][j] == '*':
            water.append((i, j))
        if forest[i][j] == 'S':
            start = (i, j)
        if forest[i][j] == 'D':
            goal = (i, j)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

#물이 차있는 위치를 순회하며 반복할 때마다 방문 리스트를 초기화하여 각 위치마다 물이 도달하는 최소 시간을 기록
for i in water:
    visited = [[False] * C for _ in range(R)]
    bfs(i[0], i[1])

#여기서부터는 고슴도치가 비버의 굴까지 이동하는 시간 기록
visited = [[False] * C for _ in range(R)]
q = deque([start])
visited[start[0]][start[1]] = True
graph[start[0]][start[1]] = 0

while q:
    r, c = q.popleft()

    for i in range(4):
        rr, cc = r+dr[i], c+dc[i]

        if 0<=rr<R and 0<=cc<C and not visited[rr][cc]:
            #다음 위치가 빈곳인데
            if forest[rr][cc] == '.':
                #다음 위치에 물이 도달하는 시간보다 고슴도치가 현재 있는 위치까지 걸린 시간+1이 작아야만 이동 가능
                if graph[r][c] + 1 < graph[rr][cc]:
                    graph[rr][cc] = True
                    graph[rr][cc] = graph[r][c] + 1
                    q.append((rr, cc))
            #다음 위치가 목적지라면
            elif forest[rr][cc] == 'D':
                visited[rr][cc] = True
                #목적지에 여러 방향에서 도착할 수 있으므로 최단시간 갱신
                graph[rr][cc] = min(graph[rr][cc], graph[r][c] + 1)

#목적지가 방문처리 되어있다면 도달 시간을 출력, 아니면 KAKTUS
if visited[goal[0]][goal[1]]:
    print(graph[goal[0]][goal[1]])
else:
    print("KAKTUS")