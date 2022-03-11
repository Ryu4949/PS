import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(N)]
check = [[0] * M for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

#bfs
#한번 탐색할 때마다 치즈의 가장자리를 확인하여 0으로 바꿔줌
def bfs(r, c):
    queue = deque([(r, c)])
    visited[r][c] = True

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            rr, cc = r+dr[i], c+dc[i]
            if 0<=rr<N and 0<=cc<M and not visited[rr][cc]:
                #다음 이동 위치가 치즈면 방문처리하고 0으로 바꿔준 후 큐에 담지 않음
                if cheese[rr][cc] == 1:
                    visited[rr][cc] = True
                    cheese[rr][cc] = 0
                #치즈가 아니라면 방문처리해주고 큐에 좌표 추가
                else:
                    visited[rr][cc] = True
                    queue.append((rr, cc))

#time에는 경과 시간, cnt_cheese에는 그때그떄 남은 치즈의 크기
#매 반복마다 방문체크 리스트를 초기화
time = 0
cnt_cheese = []
while True:
    time += 1
    visited = [[False] * M for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            cnt += cheese[i][j]

    #만약 치즈가 남아있지 않다면 time-1출력
    #마지막에 녹인 치즈의 개수는 cnt_cheese에서 가장 오른쪽 요소이므로 그거 출력
    #그리고 중단
    if cnt == 0:
        print(time-1)
        print(cnt_cheese[-1])
        break

    #치즈가 남아있다면 리스트에 치즈 크기 추가해주고 계속
    else:
        cnt_cheese.append(cnt)

    #왼쪽 가장위부터 bfs
    bfs(0, 0)

