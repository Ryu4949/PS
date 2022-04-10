import copy
def shark(sr, sc, direction, total):
    global fish, loc
    move_fish(sr, sc)   #물고기 이동

    target = search(sr, sc, direction)  #상어가 먹을 수 있는 대상
    if not target:  #상어가 먹을 수 있는 물고기가 없으면
        rlt.append(total)   #그때까지 먹은 물고기양을 rlt에 추가하고 종료
        return

    for i in target:    #먹을 수 있는 물고기가 있으면
        base_fish, base_loc = copy.deepcopy(fish), copy.deepcopy(loc)
        fr, fc = i[0], i[1]
        fish[fr][fc][2] = -1    #먹힘 처리해주고
        loc[fish[fr][fc][0]], loc[fish[sr][sc][0]] = loc[fish[sr][sc][0]], loc[fish[fr][fc][0]] #위치 정보 바꾸고
        fish[sr][sc], fish[fr][fc] = fish[fr][fc], fish[sr][sc] #그래프에서 두개 서로 바꾸고

        shark(fr, fc, fish[sr][sc][1], total+fish[sr][sc][0])   #다음 단계

        fish = base_fish    #원상복구
        loc = base_loc

def move_fish(sr, sc):  #물고기 이동
    for i in range(1, 17):
        r, c = loc[i][0], loc[i][1]
        if fish[r][c][2] == -1: #이미 먹힌 물고기면 스킵
            continue

        direction = fish[r][c][1]

        for _ in range(9):
            rr, cc = r+dr[direction], c+dc[direction]

            if 0<=rr<4 and 0<=cc<4: #범위 내인데
                if rr != sr or cc != sc:    #상어가 있는 곳이 아니면
                    fish[r][c][1] = direction
                    loc[fish[r][c][0]], loc[fish[rr][cc][0]] = loc[fish[rr][cc][0]], loc[fish[r][c][0]]
                    fish[r][c], fish[rr][cc] = fish[rr][cc], fish[r][c]
                    break

            direction = (direction+1)%8 #이동할 수 없으면 방향 반시계 45도 회전

def search(sr, sc, direction):  #상어가 먹을 수 있는 대상 탐색
    target = []
    for p in range(1, 4):
        srr, scc = sr+dr[direction]*p, sc+dc[direction]*p

        if 0 <=srr<4 and 0<=scc<4 and fish[srr][scc][2] == 0:
            target.append((srr, scc))
    return target


fish = [[[0, 0, 0] for _ in range(4)] for _ in range(4)]

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]

for i in range(4):
    data = [*map(int, input().split())]
    for j in range(4):
        fish[i][j][0] = data[2*j]
        fish[i][j][1] = data[2*j+1]-1

loc = [[0] * 2 for _ in range(17)]
for i in range(4):
    for j in range(4):
        loc[fish[i][j][0]] = [i, j]

rlt = []

fish[0][0][2] = -1

shark(0, 0, fish[0][0][1], fish[0][0][0])
print(max(rlt))