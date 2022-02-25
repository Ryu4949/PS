N = int(input())
graph = [list(map(int, list(input()))) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
cnt = 0
apt = 0
home_cnt = []

def dfs(r, c):
    global cnt

    # if r < 0 or r >= N or c < 0 or c >= N:
    #     return False
    #
    # if graph[r][c] == 1:
    #     cnt += 1
    #     graph[r][c] = 0
    #     for i in range(4):
    #         rr = r + dr[i]
    #         cc = c + dc[i]
    #         dfs(rr, cc)
    #     return True
    # return False

for i in range(N):
    for j in range(N):
        if dfs(i, j) == True:
            apt += 1
            home_cnt.append(cnt)
            cnt = 0

home_cnt.sort()
print(apt)
for i in home_cnt:
    print(i)


