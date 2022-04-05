from collections import deque

def bfs():
    queue = deque([(0, 0)])
    costs[0][0] = 0

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            rr, cc = r+dr[i], c+dc[i]
            if 0<=rr<N and 0<=cc<N:
                cost = costs[r][c]+max(graph[rr][cc]-graph[r][c], 0)+1

                if cost < costs[rr][cc]:
                    queue.append((rr, cc))
                    costs[rr][cc] = cost

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    graph = [[*map(int, input().split())] for _ in range(N)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    costs = [[float('inf')] * N for _ in range(N)]

    bfs()

    print(f'#{tc} {costs[N-1][N-1]}')
