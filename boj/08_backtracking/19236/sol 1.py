from pprint import pprint

def is_fish(r, c, d):   #상어가 이동할 수 있는 칸
    move = []
    for p in range(1, 4):
        rr, cc = r+dr[d]*p, c+dc[d]*p
        if 0<=rr<4 and 0<=cc<4 and fish[rr][cc]:
            move.append([rr, cc])
    return move

def shark(r, c, d, total): #r, c는 상어의 위치, total은 먹은 물고기 총합
    global ans

    move_fish()

    move = is_fish(r, c, d)

    if not move:    #상어가 이동할 수 있는 칸이 없으면 그만
        rlt.append(total)
        return

    for i in move:
        loc[fish[i[0]][i[1]]][2] = 0
        shark(i[0], i[1], fish[i[0]][i[1]][1], total+fish[i[0]][i[1]][0])

def move_fish():    #물고기 이동
    for i in range(1, 17):
        if not loc[i][2]:
            continue

        r, c = loc[i][0], loc[i][1]
        direction = fish[r][c][1]

        for _ in range(9):
            print(f'방향: {direction}')
            rr, cc = r+dr[direction], c+dc[direction]

            if 0<=rr<4 and 0<=cc<4 and fish[rr][cc][0] != 0:
                print(f'바꿀 물고기: {fish[rr][cc]}')
                fish[r][c][1] = direction
                loc[i][0], loc[fish[rr][cc][0]][0] = loc[fish[rr][cc][0]][0], loc[i][0]
                loc[i][1], loc[fish[rr][cc][0]][1] = loc[fish[rr][cc][0]][1], loc[i][1]
                fish[r][c], fish[rr][cc] = fish[rr][cc], fish[r][c]
                pprint(fish)
                print(loc)
                break

            direction = (direction+1)%8





dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]

loc = [0] * 17  #상어에게 먹힌 물고기 체크
fish = [[[] for _ in range(4)] for _ in range(4)]

for i in range(4):
    data = [*map(int, input().split())]
    for j in range(4):
        fish[i][j].append(data[2*j])
        fish[i][j].append(data[2*j+1]-1)

ans = 0
pprint(fish, width = 50)

for i in range(4):
    for j in range(4):
        loc[fish[i][j][0]] = [i, j, 1]

rlt = []

ans = 0

shark(0, 0, fish[0][0][1], start)
print(ans)