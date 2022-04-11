from collections import deque

def topology_sort():
    result = []
    queue = deque()

    for i in range(1, N+1):
        if indegree[i] == 0:
            queue.append((i, 1))

    while queue:
        v, s = queue.popleft()
        result.append((v, s))

        for j in edges[v]:
            indegree[j] -= 1

            if indegree[j] == 0:
                queue.append((j, s+1))

    return result

N, M = map(int, input().split())
indegree = [0] * (N+1)
edges = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    edges[a].append(b)
    indegree[b] += 1

rlt = topology_sort()
rlt.sort()

for i in rlt:
    print(i[1], end=' ')