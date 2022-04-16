#이분탐색 + bfs 틀렸다가 맞음
#절대값 처음에 빼먹어서

from collections import deque
def bfs(slope):
    visited = [[False] * N for _ in range(N)]
    visited[0][0] = True
    queue = deque([(0, 0)])

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            rr, cc = r+dr[i], c+dc[i]

            if 0<=rr<N and 0<=cc<N and not visited[rr][cc] and abs(graph[rr][cc]-graph[r][c]) <= slope:
                queue.append((rr, cc))
                visited[rr][cc] = True

    return visited[N-1][N-1]

N = int(input())
graph = [[*map(int, input().split())] for _ in range(N)]

start = 0
end = 10**9+1

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

ans = 0
while start <= end:
    mid = (start+end)//2
    if bfs(mid):
       ans = mid
       end = mid-1
    else:
       start = mid+1

print(ans)