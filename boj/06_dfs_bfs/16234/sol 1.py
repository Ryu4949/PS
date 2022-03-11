import sys
from collections import deque
input = sys.stdin.readline

N, L, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

#상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

#move는 하루동안 인구이동이 한번이라도 발생했는지 체크하는 변수
#cnt는 연합내 국가의 수, population은 연합내 국가의 인구 수의 합, country는 연합에 소속된 국가의 좌표를 담을 리스트
def bfs(r, c):
    global move
    queue = deque([(r, c)])
    visited[r][c] = True
    population = graph[r][c]
    cnt = 1
    country = [(r, c)]

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            rr, cc = r+dr[i], c+dc[i]
            if 0<=rr<N and 0<=cc<N and not visited[rr][cc]:
                #인접 국가와의 차이가 L이상 R이하라면 국경이 열리므로
                if L<=abs(graph[r][c] - graph[rr][cc])<=R:
                    #방문처리하고, 큐에 추가하고, 국가수 1 증가, 인구 더해주고, 연합국 목록에 추가하고
                    #인구 이동이 발생했으므로 move = True로 바꿔줌
                    visited[rr][cc] = True
                    queue.append((rr, cc))
                    cnt += 1
                    population += graph[rr][cc]
                    country.append((rr, cc))
                    move = True

    #bfs를 마치고나면 연합 소속 국가들의 인구를 동일하게 조정
    for i in country:
        graph[i[0]][i[1]] = population // cnt

#day는 인구이동이 며칠간 발생했는지 저장할 변수
day = 0
while True:
    #반복때마다 방문 체크 리스트와 인구이동 여부 초기화
    move = False
    visited = [[False] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                bfs(i, j)

    #인구이동이 발생했으면 day에 1추가하고 다시 반복
    if move == True:
        day += 1
    #인구 이동이 발생하지 않았으면 중단
    else:
        break

print(day)