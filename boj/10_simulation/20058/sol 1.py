from pprint import pprint
import copy

def adj_ice(r, c):   #(r, c)에 인접한 얼음이 있는 칸의 수
    cnt = 0
    for i in range(4):
        rr, cc = r+dr[i], c+dc[i]
        if 0<=rr<size and 0<=cc<size and graph[rr][cc] > 0:
            cnt += 1
    return cnt

def rotate(r, c, interval): #왼쪽 위 좌표가 (r, c)이고 가로세로 길이가 interval인 배열을 회전
    for i in range(interval):
        for j in range(interval):
            graph[r+j][c+interval-i-1] = base[r+i][c+j]

def dfs(r, c):
    global ice, ans
    stack = [(r, c)]
    visited[r][c] = True
    area = 1
    ice += graph[r][c]

    while stack:
        r, c = stack.pop()
        for i in range(4):
            rr, cc = r+dr[i], c+dc[i]

            if 0<=rr<size and 0<=cc<size and graph[rr][cc] > 0 and not visited[rr][cc]:
                stack.append((rr, cc))
                visited[rr][cc] = True
                area += 1
                ice += graph[rr][cc]
    ans = max(ans, area)


N, Q = map(int, input().split())
size = 2**N
graph = [[*map(int, input().split())] for _ in range(size)]
step = [*map(int, input().split())]
visited = [[False]*size for _ in range(size)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

cnt = 0
while True:
    cnt += 1
    interval = 2**step[cnt-1]
    base = copy.deepcopy(graph)
    for i in range(size//interval):
        for j in range(size//interval):
            rotate(interval*i, interval*j, interval)

    cnt_ice = [[0]*size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            cnt_ice[i][j] = adj_ice(i, j)

    for i in range(size):
        for j in range(size):
            if cnt_ice[i][j] < 3:
                graph[i][j] -= 1

    if cnt == Q:
        break

ice = 0
ans = 0

for i in range(size):
    for j in range(size):
        if graph[i][j] > 0 and not visited[i][j]:
            dfs(i, j)

print(ice)
print(ans)