dr = [-1, -1, -1, 0, 1, 1, 1, 0]
dc = [-1, 0, 1, 1, 1, 0, -1, -1]

# def dfs(r, c):
#     if 0<=r<H and 0<=c<W and graph[r][c] == 1:
#         graph[r][c] = 0
#         for i in range(8):
#             rr, cc = r+dr[i], c+dc[i]
#             dfs(rr, cc)
#         return True
#     return False

def dfs(r, c):
    global cnt
    if graph[r][c] == 1:
        cnt += 1
        stack = [(r, c)]
        graph[r][c] = 0
        while stack:
            r, c = stack.pop()
            for i in range(8):
                rr, cc = r+dr[i], c+dc[i]
                if 0<=rr<H and 0<=cc<W and graph[rr][cc] == 1:
                    stack.append((rr, cc))
                    graph[rr][cc] = 0


while True:
    W, H = map(int, input().split())
    if W == 0 and H == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(H)]

    cnt = 0
    for i in range(H):
        for j in range(W):
            if dfs(i, j):
                cnt += 1

    print(cnt)