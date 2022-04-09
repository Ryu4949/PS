def diffuse(r, c):  #r, c위치에서 확산
    if dust[r][c][0] == -1: #청정기 칸이면 pass
        return

    fifth = dust[r][c][0] // 5
    for i in range(4):
        rr, cc = r+dr[i], c+dc[i]
        if 0<=rr<R and 0<=cc<C and graph[rr][cc] != -1:
            dust[rr][cc][1] += fifth
            dust[r][c][0] -= fifth

def rotate(r, c, d, graph): #회전
    rr, cc = r+dr[d], c+dc[d]
    if graph[rr][cc][0] == -1:
        graph[r][c][0] = 0
    else:
        graph[rr][cc][0] = graph[r][c][0]
        graph[r][c][0] = 0

def upside():   #위쪽 구역 순환
    ux = up[0]-1
    uy = 0
    direction = 0

    while True:
        rotate(ux, uy, (direction+2)%4, dust)

        if 0<=ux+dr[direction]<=up[0] and 0<=uy+dc[direction]<C:
            ux += dr[direction]
            uy += dc[direction]
        else:
            direction = (direction+1)%4
            ux += dr[direction]
            uy += dc[direction]

        if ux == up[0] and uy == up[1]:
            return

def downside(): #아래쪽 구역 순환
    dx = down[0]+1
    dy = 0
    direction = 2

    while True:
        rotate(dx, dy, (direction+2)%4, dust)

        if down[0]<=dx+dr[direction]<R and 0<=dy+dc[direction]<C:
            dx += dr[direction]
            dy += dc[direction]
        else:
            direction = (direction-1)%4
            dx += dr[direction]
            dy += dc[direction]

        if dx == down[0] and dy == down[1]:
            return

R, C, T = map(int, input().split())
dust = [[[0, 0] for _ in range(C)] for _ in range(R)]
graph = [[*map(int, input().split())] for _ in range(R)]
for i in range(R):
    for j in range(C):
        dust[i][j][0] = graph[i][j]

up = None
down = None

for i in range(R):
    if graph[i][0] == -1:
        up = (i, 0)
        down = (i+1, 0)
        break

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

time = 0
while True:
    time += 1

    for i in range(R):
        for j in range(C):
            diffuse(i, j)

    for i in range(R):
        for j in range(C):
            dust[i][j][0] += dust[i][j][1]
            dust[i][j][1] = 0

    upside()
    downside()

    if time == T:
        break

ans = 0
for i in range(R):
    for j in range(C):
       ans += dust[i][j][0]

print(ans+2)