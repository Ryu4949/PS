#시간초과

import sys
input = sys.stdin.readline

def dfs(r, c, n):
    global answer
    answer = max(answer, n)

    #이부분 있어도 시간초과
    if answer == 26:
        print(26)
        exit()

    for i in range(4):
        rr, cc = r+dr[i], c+dc[i]
        if 0<=rr<R and 0<=cc<C and board[rr][cc] not in alphaset:
            alphaset.add(board[rr][cc])
            dfs(rr, cc, n+1)
            alphaset.remove(board[rr][cc])

R, C = map(int, input().split())
board = [list(input().rstrip()) for _ in range(R)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

alphaset = set()
alphaset.add(board[0][0])

answer = 1

dfs(0, 0, 1)

print(answer)