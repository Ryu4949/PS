board = [list(input().split()) for _ in range(5)]
num_list = []

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c, num):
    if len(num) == 6:
        num_list.append(num)
        return

    for i in range(4):
        rr, cc = r+dr[i], c+dc[i]
        if 0<=rr<5 and 0<=cc<5:
            dfs(rr, cc, num+board[rr][cc])
            #여기 dfs 앞에 return 붙이면 이상하게 나옴

for i in range(5):
    for j in range(5):
        dfs(i, j, board[i][j])

print(len(set(num_list)))