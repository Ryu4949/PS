import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

#time에는 각 위치가 바이러스에 감염되는 시간
time = [[0] * N for _ in range(N)]
S, X, Y = map(int, input().split())

#최초 바이러스의 좌표를 담아줄 리스트
virus = []

#입력 데이터를 확인하면서 0이 아닌 경우 (바이러스 종류, 행, 열, 0)을 담아줌
#0은 시간 계산에 활용
for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            virus.append((graph[i][j], i, j, 0))

#1번 바이러스부터 처리할 수 있도록 정렬
virus.sort()

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs():
    queue = deque(virus)

    while queue:
        s, r, c, t = queue.popleft()

        for i in range(4):
            rr, cc = r+dr[i], c+dc[i]
            #다음칸이 범위 내이고 아직 감염되지 않은 칸이라면
            if 0<=rr<N and 0<=cc<N and graph[rr][cc] == 0:
                #같은 종류의 바이러스로 감염, 1초 늘어난 시간 처리 후 큐에 추가
                graph[rr][cc] = s
                time[rr][cc] = t + 1
                queue.append((s, rr, cc, t+1))

bfs()

#확인 지점에서 감염에 걸리는 시간이 S보다 작거나 같다면 해당 위치의 바이러스 종류 출력
if time[X-1][Y-1] <= S:
    print(graph[X-1][Y-1])
else:
    print(0)