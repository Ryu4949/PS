from collections import deque

def bfs(r, c):
    queue = deque()
    queue.append((r, c, 0, 0))  #위치좌표, 열쇠, 이동횟수
    visited[r][c] = 0

    while queue:
        r, c, key, cnt = queue.popleft()

        for i in range(4):
            rr, cc = r+dr[i], c+dc[i]

            if 0<=rr<N and 0<=cc<M and graph[rr][cc] != '#' and visited[rr][cc] != key:
                if graph[rr][cc].islower():
                    queue.append((rr, cc, key|(1<<keys[graph[rr][cc]]), cnt+1))
                    visited[rr][cc] = key|(1<<keys[graph[rr][cc]])
                elif graph[rr][cc].isupper() and key & (1<<doors[graph[rr][cc]]):
                    queue.append((rr, cc, key, cnt+1))
                    visited[rr][cc] = key
                elif graph[rr][cc] == '.' or graph[rr][cc] == '0':
                    queue.append((rr, cc, key, cnt+1))
                    visited[rr][cc] = key
                elif graph[rr][cc] == '1':
                    return cnt+1
    return -1

N, M = map(int, input().split())
graph = [list(input()) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if graph[i][j] == '0':
            sx, sy = i, j
            break

keys = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5}
doors = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5}

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

visited = [[-1] * M for _ in range(N)]

print(bfs(sx, sy))
