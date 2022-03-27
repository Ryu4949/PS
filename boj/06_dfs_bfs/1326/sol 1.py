from collections import deque

N = int(input())
stones = [0] + list(map(int, input().split()))
S, G = map(int, input().split())

visited = [-1] * (N+1)

def bfs(v):
    queue = deque([v])
    visited[v] = 0

    while queue:
        v = queue.popleft()

        for i in range(1, N+1):
            if abs(i-v) % stones[v] == 0 and visited[i] == -1:
                if i == G:
                    return visited[v] + 1
                queue.append(i)
                visited[i] = visited[v] + 1

    return -1

print(bfs(S))