#그래프를 만들어 줄 땐 양쪽 모두에 추가!!
#ex) 1과 2가 연결되어있으면 1에는 2를, 2에는 1을 각각 추가
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
visited = [False] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(graph, 1, visited)

print(visited.count(True)-1)