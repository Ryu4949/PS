#시간초과

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

visited = [[0] * M for _ in range(N)]
def dfs():
    stack = [(0, 0)]
    visited[0][0] = 1

    while stack:
        r, c = stack.pop()

        for i in range(4):
            rr, cc = r+dr[i], c+dc[i]

            if 0<=rr<N and 0<=cc<M and graph[rr][cc] < graph[r][c]:
                stack.append((rr, cc))
                visited[rr][cc] += 1

dfs()

print(visited[-1][-1])