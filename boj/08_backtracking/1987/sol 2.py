#통과
#이미 문자열이 나왔는지 확인하는데 set을 이용하면 시간복잡도 측면에서 효율적이라고 생각했는데 꼭 그렇진 않은가보다

import sys
input = sys.stdin.readline

def dfs(r, c, n):
    global answer
    answer = max(answer, n)

    if answer == 26:
        print(26)
        exit()

    for i in range(4):
        rr, cc = r+dr[i], c+dc[i]
        if 0<=rr<R and 0<=cc<C and not check[ord(board[rr][cc])-65]:
            check[ord(board[rr][cc])-65] = True
            dfs(rr, cc, n+1)
            check[ord(board[rr][cc])-65] = False

R, C = map(int, input().split())
board = [list(input().rstrip()) for _ in range(R)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
check = [False] * 26

check[ord(board[0][0])-65] = True
answer = 1

dfs(0, 0, 1)

print(answer)