from pprint import pprint

def melt():
    for r in range(N):
        for c in range(M):
            if graph[r][c] > 0:
                for i in range(4):
                    rr, cc = r+dr[i], c+dc[i]
                    if 0<=rr<N and 0<=cc<M and graph[rr][cc] == 0:
                        graph[r][c] -= 1
                        if graph[r][c] == 0:
                            break

#
#
# def dfs(r, c):
#     stack = [(r, c)]
#     visited[r][c] = True

N, M = map(int, input().split())
graph = [[*map(int, input().split())] for _ in range(N)]
pprint(graph)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

melt()
pprint(graph)