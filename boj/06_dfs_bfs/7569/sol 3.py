import sys
from collections import deque
input = sys.stdin.readline

db = [0, 0, 0, 0, -1, 1]
dr = [-1, 1, 0, 0, 0, 0]
dc = [0, 0, -1, 1, 0, 0]

def bfs():
    queue = deque(tomato)
    for i, j, k in queue:
        check[i][j][k] = 0

    while queue:
        b, r, c = queue.popleft()

        for i in range(6):
            bb, rr, cc = b+db[i], r+dr[i], c+dc[i]
            if 0<=bb<H and 0<=rr<N and 0<=cc<M:
                if box[bb][rr][cc] == 0:
                    check[bb][rr][cc] = check[b][r][c]+1
                    box[bb][rr][cc] = 1
                    queue.append((bb, rr, cc))

#박스안에 0이 존재하는지 확인하는 함수
#처음에 모든 토마토가 익어있는지 확인할 때 사용하고
#마지막에 bfs를 마치고도 안익은 토마토가 존재하는지 확인할 때 사용
def unripe(arr):
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if arr[i][j][k] == 0:
                    return True
    return False



M, N, H = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
check = [[[-1] * M for _ in range(N)] for _ in range(H)]

#처음에 토마토가 존재하는 위치 저장
tomato = []
for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 1:
                tomato.append((i, j, k))

#탐색을 하기 전에 안익은 토마토가 하나도 없다면 0을 출력하고 종료
if not unripe(box):
    print(0)
    exit()

bfs()

#탐색을 마친 후에 안익은 토마토가 존재한다면 -1을 출력
if unripe(box):
   print(-1)
   
#모두 익었다면 check리스트를 순회하면서 최대값 출력
else:
    ans = 0
    for i in range(H):
        for j in range(N):
            for k in range(M):
                ans = max(ans, check[i][j][k])

    print(ans)