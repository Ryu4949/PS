from collections import deque
import sys
input = sys.stdin.readline

def bfs(r, c):
    queue = deque()
    queue.append((r, c, 0, 0))
    visited[r][c][0] = 1

    while queue:
        r, c, key, cnt = queue.popleft()

        for i in range(4):
            rr, cc = r+dr[i], c+dc[i]

            if 0<=rr<N and 0<=cc<M and graph[rr][cc] != '#' and not visited[rr][cc][key]:
                if graph[rr][cc] == '.':
                    visited[rr][cc][key] = 1
                    queue.append((rr, cc, key, cnt+1))
                elif graph[rr][cc].islower():
                    new_key = key|(1<<ord(graph[rr][cc])-97)
                    if not visited[rr][cc][new_key]:
                        visited[rr][cc][new_key] = 1
                        queue.append((rr, cc, new_key, cnt+1))
                elif graph[rr][cc].isupper() and key&(1<<(ord(graph[rr][cc])-65)):
                    visited[rr][cc][key] = 1
                    queue.append((rr, cc, key, cnt+1))
                elif graph[rr][cc] == '1':
                    return cnt+1
    return -1



N, M = map(int, input().split())
graph = [list(input().strip()) for _ in range(N)]
visited = [[[0]*(1<<6) for _ in range(M)] for _ in range(N)]

for i in range(N):
    for j in range(M):
        if graph[i][j] == '0':
            sx, sy = i, j
            graph[i][j] = '.'
            break

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

print(bfs(sx, sy))