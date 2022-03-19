from collections import deque

def bfs(v):
    queue = deque([v])
    visited[v][0] = 0
    visited[v][1] = 1

    while queue:
        v = queue.popleft()
        dv = [v-1, v+1, 2*v]

        for i in dv:
            if 0<=i<=100000:
                if visited[i][0] == -1:
                    queue.append(i)
                    visited[i][0] = visited[v][0] + 1
                    visited[i][1] = visited[v][1]

                elif visited[i][0] == visited[v][0] + 1:
                    visited[i][1] += visited[v][1]

N, K = map(int, input().split())
visited = [[-1, 0] for _ in range(100001)]

bfs(N)

print(visited[K][0])
print(visited[K][1])