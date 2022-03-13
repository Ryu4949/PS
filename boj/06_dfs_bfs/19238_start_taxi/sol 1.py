import sys
input = sys.stdin.readline
from collections import deque
import heapq

#택시가 있는 위치에서 각 위치별로 최단거리를 계산하고, 그 과정에서 손님이 있다면 guest_list에 담아줌
def bfs(r, c):
    global fuel, tx, ty

    visited = [[False] * N for _ in range(N)]
    queue = deque([(0, r, c)])
    visited[r][c] = True
    guest_list = []

    #처음 택시가 있는 위치에 손님이 있다면 여기서 바로 추가// (최단거리, 출발 행, 출발 열, 도착 행, 도착 열)을 저장
    if graph[r][c] > 0:
        heapq.heappush(guest_list, (0, guests[graph[r][c]-1][0], guests[graph[r][c]-1][1], guests[graph[r][c]-1][2], guests[graph[r][c]-1][3]))

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
        #거리만큼 연료 차감하고, 연료가 음수가 되면 -1출력하고 바로 종료
        fuel -= d
        if fuel < 0:
            print(-1)
            exit()

        #출발지를 0으로 바꿈
        graph[sx][sy] = 0

        #출발지에서 도착지의 거리보다 남은 연료가 작다면 목적지에 도착할 수 없으므로 -1 출력하고 종료
        if fuel < distance(sx, sy, dx, dy):
            print(-1)
            exit(0)

        #출발지에서 도착지까지 벽으로 인해 도착할 수 없다면 -1출력하고 종료
        elif distance(sx, sy, dx, dy) == -1:
            print(-1)
            exit(0)

        #도착 가능하다면 거리만큼 연료에 더해주고, 택시의 위치를 도착지의 좌표로 갱신
        fuel += distance(sx, sy, dx, dy)
        tx = dx
        ty = dy

#(sx, sy)로부터 (dx, dy)로의 최단거리. 위의 함수에서 같이 처리하고 싶었는데 헷갈려서 나눔
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

                #도착지에 도착하면 거리를 반환
                if rr == dx and cc == dy:
                    return d + 1

    #탐색이 끝나도록 도착지가 방문처리되지 않으면 도달할 수 없는 경우고, -1을 반환
    if not visited[dx][dy]:
        return -1

N, M, F = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
tx, ty = map(int, input().split())
guests = [list(map(int, input().split())) for _ in range(M)]

#택시의 위치와 손님의 출발위치, 도착위치를 -1씩 해줌(인덱스로 쓸 수 있도록)
tx -= 1
ty -= 1

for i in range(M):
    guests[i] = list(map(lambda x: x-1, guests[i]))

#벽을 1에서 X로 바꿈
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            graph[i][j] = 'X'

#각 손님의 출발위치에 손님 번호 표시
for i in range(M):
    graph[guests[i][0]][guests[i][1]] = i+1

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

fuel = F

#손님들의 정보를 확인하면서 택시가 태우러 갈 수 없는 손님이 있다면 -1출력하고 종료
for i in guests:
    if distance(tx, ty, i[0], i[1]) == -1:
        print(-1)
        exit(0)

#택시가 더이상 이동할 수 없을 때까지 bfs 반복하고 종료시점의 연료 출력
while True:
    if bfs(tx, ty) == -1:
        print(fuel)
        break

    else:
        bfs(tx, ty)
