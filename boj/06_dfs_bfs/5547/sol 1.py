from collections import deque
#건물이 없는 칸을 카운트!
W, H = map(int, input().split())
graph = [[0] * (W+1)]
for _ in range(H):
    graph.append([0] + list(map(int, input().split())))
visited = [[False] * (W+1) for _ in range(H+1)]

#h가 짝수일 때
dh = [-1, 0, 1, 0, -1, -1]
dw = [-1, -1, 0, 1, 1, 0]

#h가 홀수일 때
dh2 = [0, 1, 1, 1, 0, -1]
dw2 = [-1, -1, 0, 1, 1, 0]

def bfs(h, w):
    queue = deque([h, w])
    visited[h][w] = True
    cnt = 0

    while queue:
        h, w = queue.popleft()
        if h % 2 == 0:
            for i in range(6):
                hh = h +
