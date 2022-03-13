#아직 틀림

import sys
input = sys.stdin.readline
from collections import deque
import heapq

#상어가 현재 있는 위치에서 다른 위치로의 최단거리를 찾고, 그 과정에서 먹을 수 있는 물고기는 따로 목록 작성
def bfs(r, c):
    global fuel, tx, ty

    visited = [[False] * N for _ in range(N)]
    queue = deque([(0, r, c)])
    visited[r][c] = True
    guest_list = []

    #(r, c)기준 다른 위치로의 최단거리 탐색
    while queue:
        d, r, c = queue.popleft()

        for i in range(4):
            rr, cc = r+dr[i], c+dc[i]

            if 0<=rr<N and 0<=cc<N and not visited[rr][cc] and graph[rr][cc] != 'X':
                queue.append((d+1, rr, cc))
                visited[rr][cc] = True

                if graph[rr][cc] > 0:
                    heapq.heappush(guest_list, (d+1, guests[graph[rr][cc]-1][0], guests[graph[rr][cc]-1][1], guests[graph[rr][cc]-1][2], guests[graph[rr][cc]-1][3]))

    # 손님을 모두 태워줬다면
    if not guest_list:
        return -1

    # 남아있다면
    else:
        d, sx, sy, dx, dy = heapq.heappop(guest_list)
        fuel -= d
        if fuel < 0:
            print(-1)
            exit()

        graph[sx][sy] = 0

        if fuel < distance(sx, sy, dx, dy):
            print(-1)
            exit(0)

        elif distance(sx, sy, dx, dy) == -1:
            print(-1)
            exit(0)

        fuel += distance(sx, sy, dx, dy)
        tx = dx
        ty = dy

def distance(sx, sy, dx, dy):
    visited = [[False] * N for _ in range(N)]
    queue = deque([(0, sx, sy)])
    visited[sx][sy] = True

    while queue:
        d, r, c = queue.popleft()

        for i in range(4):
            rr, cc = r + dr[i], c + dc[i]

            if 0 <= rr < N and 0 <= cc < N and not visited[rr][cc] and graph[rr][cc] != 'X':
                queue.append((d + 1, rr, cc))
                visited[rr][cc] = True

                if rr == dx and cc == dy:
                    return d + 1

    if not visited[dx][dy]:
        return -1

N, M, F = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
tx, ty = map(int, input().split())
guests = [list(map(int, input().split())) for _ in range(M)]

tx -= 1
ty -= 1

for i in range(M):
    guests[i] = list(map(lambda x: x-1, guests[i]))

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            graph[i][j] = 'X'

for i in range(M):
    graph[guests[i][0]][guests[i][1]] = i+1

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

fuel = F

for i in guests:
    if distance(tx, ty, i[0], i[1]) == -1:
        print(-1)
        exit(0)

while True:
    if bfs(tx, ty) == -1:
        print(fuel)
        break

    else:
        bfs(tx, ty)
