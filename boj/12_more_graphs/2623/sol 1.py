from collections import deque
import sys
input = sys.stdin.readline

def topology_sort():
    result = []
    queue = deque()

    for i in range(1, N+1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        now = queue.popleft()
        result.append(now)

        for j in graph[now]:
            indegree[j] -= 1

            if indegree[j] == 0:
                queue.append(j)

    if len(result) == N:
        for i in result:
            print(i)
    else:
        print(0)

N, M = map(int, input().split())
indegree = [0] * (N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    order = [*map(int, input().split())]
    for i in range(1, order[0]):
        if order[i+1] not in graph[order[i]]:
            graph[order[i]].append(order[i+1])
            indegree[order[i+1]] += 1

topology_sort()
