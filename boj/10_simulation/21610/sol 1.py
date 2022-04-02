from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[*map(int, input().split())] for _ in range(N)]
order = [[*map(int, input().split())] for _ in range(M)]

dr = [0, -1, -1, -1, 0, 1, 1, 1]
dc = [-1, -1, 0, 1, 1, 1, 0, -1]

drr = [-1, -1, 1, 1]
dcc = [-1, 1, 1, -1]

cloud = deque([[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]])
move = 0

while True:
    visited = [[False] * N for _ in range(N)]
    for i in cloud:
        i[0] = (i[0] + dr[order[move][0]-1] * order[move][1]) % N
        i[1] = (i[1] + dc[order[move][0]-1] * order[move][1]) % N
        graph[i[0]][i[1]] += 1
        visited[i[0]][i[1]] = True

    for r, c in cloud:
        for i in range(4):
            rr, cc = r+drr[i], c+dcc[i]
            if 0<=rr<N and 0<=cc<N and graph[rr][cc] > 0:
                graph[r][c] += 1

    num_cloud = len(cloud)

    for i in range(N):
        for j in range(N):
            if not visited[i][j] and graph[i][j] >= 2:
                graph[i][j] -= 2
                cloud.append([i, j])

    for _ in range(num_cloud):
        cloud.popleft()

    move += 1

    if move == M:
        break

ans = 0
for i in range(N):
    for j in range(N):
        ans += graph[i][j]

print(ans)