import sys
input = sys.stdin.readline
from collections import deque
import heapq

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

size = 2
eat = 0
time = 0

#처음 상어의 위치
for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            sx = i
            sy = j

#상어가 현재 있는 위치에서 다른 위치로의 최단거리를 찾고, 그 과정에서 먹을 수 있는 물고기는 따로 목록 작성
def bfs(r, c):
    global size, eat, time, sx, sy

    visited = [[False] * N for _ in range(N)]
    queue = deque([(0, r, c)])
    visited[r][c] = True
    fish = []
    graph[r][c] = 0

    while queue:
        d, r, c = queue.popleft()

        for i in range(4):
            rr, cc = r+dr[i], c+dc[i]

            if 0<=rr<N and 0<=cc<N and not visited[rr][cc] and graph[rr][cc] <= size:
                queue.append((d+1, rr, cc))
                visited[rr][cc] = True

                if 0< graph[rr][cc] < size:
                    heapq.heappush(fish, (d+1, rr, cc))

    #먹을 생선이 남아있지 않다면
    if not fish:
        return -1

    #남아있다면
    else:
        #거리가 가장 가까운 물고기를 pop 해서
        #eat증가, 시간을 이동거리만큼 더해주고, 먹은 위치를 상어인 9로 바꿔주고, sx, sy를 현재 위치로 갱신
        d, r, c = heapq.heappop(fish)
        eat += 1
        time += d
        graph[r][c] = 9
        sx, sy = r, c

        #먹은 물고기수가 사이즈와 같다면 사이즈 1 증가시켜주고, eat은 다시 0으로 초기화
        if eat == size:
            eat = 0
            size += 1

while True:
    if bfs(sx, sy) == -1:
        break
    else:
        bfs(sx, sy)

print(time)

