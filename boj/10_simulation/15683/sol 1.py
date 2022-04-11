

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
camera = [
    [],
    [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]],
    [[1, 1, 0, 0],[0, 0, 1, 1]],
    [[1, 0, 1, 0],[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 0, 1]],
    [[1, 1, 1, 0], [1, 0, 1, 1], [0, 1, 1, 1], [1, 1, 0, 1]],
    [[1, 1, 1, 1]]
]

N, M = map(int, input().split())
graph = [[*map(int, input().split())] for _ in range(N)]
loc = []
for i in range(N):
    for j in range(N):
        if graph[i][j] in range(1,6):
            loc.append((i, j, graph[i][j]))

print(loc)

cameras = []
for i in loc:
    cameras += camera[i[2]]
print(cameras)