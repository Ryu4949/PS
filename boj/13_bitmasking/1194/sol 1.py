#솔직히 뭐가 그리 다른지 모르겠는데 통과가 안됨
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
                if graph[rr][cc] == '.':
                    queue.append((rr, cc, key, cnt+1))
                    visited[rr][cc] = key
                elif 'a'<=graph[rr][cc]<='f':
                    new_key = key|1<<(ord(graph[rr][cc])-97)
                    queue.append((rr, cc, new_key, cnt+1))
                    visited[rr][cc] = new_key
                elif 'A'<=graph[rr][cc]<='F' and key & (1<<(ord(graph[rr][cc])-65)):
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
            graph[i][j] = '.'
            break

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

visited = [[-1] * M for _ in range(N)]

print(bfs(sx, sy))
