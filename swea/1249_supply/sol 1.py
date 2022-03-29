import heapq

def dijkstra():
    q = []
    distance[0][0] = 0
    heapq.heappush(q, (0, 0, 0))

    while q:
        dist, r, c = heapq.heappop(q)

        if distance[r][c] < dist:
            continue

        for i in range(4):
            rr, cc = r+dr[i], c+dc[i]

            if 0<=rr<N and 0<=cc<N:
                cost = graph[rr][cc] + dist
                if cost < distance[rr][cc]:
                    distance[rr][cc] = cost
                    heapq.heappush(q, (cost, rr, cc))

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    graph = [list(map(int, list(input()))) for _ in range(N)]
    INF = int(1e9)

    distance = [[INF] * N for _ in range(N)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    dijkstra()

    print(f'#{tc} {distance[N-1][N-1]}')