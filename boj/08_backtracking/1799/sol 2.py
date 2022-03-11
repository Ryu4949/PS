'''
필요한거 visited
입력 체스판

visited에는
1. 일단 처음에 비숍을 놓을 수 없는 곳은 True
2. 하나씩 놓을 때 True로 방문처리
3. 놓은 곳으로부터 대각선 방문처리
4. 다음 depth에 대해 진행시키고
5. visited 원상복구

왼쪽 위부터 하나씩 비숍을 놓고 다음 단계 진행
'''

import sys
input = sys.stdin.readline

N = int(input())
chess = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
cnt = 0
ans = []

#체스판 0인 곳은 먼저 방문처리
for i in range(N):
    for j in range(N):
        if chess[i][j] == 0:
            visited[i][j] = True

dr = [-1, -1, 1, 1]
dc = [-1, 1, 1, -1]

#(r, c)에 비숍을 놓았을 때 그 대각선 방향으로 방문처리 해주는 함수
def check(r, c):
    for i in range(4):
        p = 0
        while True:
            rr, cc = r+dr[i]*p, c+dc[i]*p
            if 0<=rr<N and 0<=cc<N:
                visited[rr][cc] = True
                p += 1
            else:
                break

def dfs(i, j):
    global cnt, visited

    if i == N:
        ans.append(cnt)
        return

    base = [i[:] for i in visited]
    if j < N-1:
        dfs(i, j+1)
        if not visited[i][j]:
            check(i, j)
            cnt += 1
            dfs(i, j+1)
            visited = base
            cnt -= 1

    else:
        dfs(i+1, 0)
        if not visited[i][j]:
            check(i, j)
            cnt += 1
            dfs(i+1, 0)
            visited = base
            cnt -= 1

dfs(0, 0)

print(max(ans))