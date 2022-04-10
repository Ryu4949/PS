from collections import deque

def topology_sort():
    result = []
    queue = deque()

    for i in range(1, N+1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        v = queue.popleft()
        result.append(v)

        for j in edges[v]:
            indegree[j] -= 1

            if indegree[j] == 0:
                queue.append(j)

    for node in result:
        print(node, end=' ')

N, M = map(int, input().split())
indegree = [0] * (N+1)
edges = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    edges[a].append(b)
    indegree[b] += 1

topology_sort()