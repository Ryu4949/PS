import sys
import heapq

N, M, K, X = map(int, sys.stdin.readline().split())
INF = int(1e9)

#출발점으로부터 도달점의 최단거리를 담을 리스트
distance = [INF] * (N+1)

graph = [[] for _ in range(N+1)]

#거리는 전부 1이기 때문에 1을 같이 담아줌
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append((b, 1))

def dijkstra(start):
    q = []

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        #이미 처리한 노드라면 무시
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            #최단거리가 변경된다면 우선순위 큐에 추가
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(X)

if distance.count(K) != 0:
    for i in range(1, N+1):
        if distance[i] == K:
            print(i)
else:
    print(-1)
