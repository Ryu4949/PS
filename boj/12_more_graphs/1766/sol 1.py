import heapq
import sys
input = sys.stdin.readline

def topology_sort():
    result = []
    q = []
    for i in range(1, N+1):
        if indegree[i] == 0:
            heapq.heappush(q, i)    #가능하면 쉬운 문제를 먼저 풀어야하니까 우선순위 큐 사용

    while q:
        v = heapq.heappop(q)
        result.append(v)

        for j in graph[v]:
            indegree[j] -= 1

            if indegree[j] == 0:
                heapq.heappush(q, j)

    return result

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

ans = topology_sort()
print(*ans)