N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
T = int(input())

screen = [[] for _ in range(N)]

for i in range(N):
    for j in range(M):
        if sum(graph[i][3*j:3*j+3]) >= T*3:
            screen[i].append(255)
        else:
            screen[i].append(0)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

ans = 0
def dfs(r, c):
    global ans

    if screen[r][c] == 0:
        return

    ans += 1
    stack = [(r, c)]
    screen[r][c] = 0

    while stack:
        r, c = stack.pop()
        for i in range(4):
            rr, cc = r+dr[i], c+dc[i]
            if 0<=rr<N and 0<=cc<M and screen[rr][cc] == 255:
                stack.append((rr, cc))
                screen[rr][cc] = 0

for i in range(N):
    for j in range(M):
        dfs(i, j)
print(ans)