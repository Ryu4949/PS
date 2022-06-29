import sys
input = sys.stdin.readline

def dfs(r, c):
    if length[r][c]:
        return length[r][c]

    length[r][c] = 1
    for i in range(4):
        rr, cc = r+dr[i], c+dc[i]

        if 0<=rr<N and 0<=cc<N and graph[rr][cc] > graph[r][c]:
            length[r][c] = max(length[r][c], dfs(rr, cc)+1)

    return length[r][c]

N = int(input())
graph = [[*map(int, input().split())] for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

length = [[0] * N for _ in range(N)]

answer = 0
for i in range(N):
    for j in range(N):
        answer = max(answer, dfs(i, j))

print(answer)
