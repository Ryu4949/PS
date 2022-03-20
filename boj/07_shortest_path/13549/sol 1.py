import heapq

N, K = map(int, input().split())
distance = [float('inf')] * 100001

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in [(1, now-1), (1, now+1), (0, 2*now)]:
            if 0<=i[1]<=100000:
                cost = dist + i[0]

                if cost < distance[i[1]]:
                    distance[i[1]] = cost
                    heapq.heappush(q, (cost, i[1]))

dijkstra(N)

print(distance[K])