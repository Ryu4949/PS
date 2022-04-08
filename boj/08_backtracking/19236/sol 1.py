from pprint import pprint

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
loc[0] = [0, 0, 1]
print(loc)


def is_fish(r, c, d):   #상어가 이동할 수 있는 물고
    for p in range(1, 4):
        rr, cc = r+dr[d]*p, c+dc[d]*p
        if 0<=rr<4 and 0<=cc<4 and loc[fish[rr][cc][0]][2]:
            return True
    return False

ans = 0

def shark(r, c, d, total): #r, c는 상어의 위치, total은 먹은 물고기 총합
    global ans

    move_fish()

    if not is_fish(r, c, d):    #상어가 이동할 수 있는 칸이 없으면 그만
        ans = max(ans, total)
        return

    for i in range(1, 4):
        rr, cc = r+dr[d]*i, c+dc[d]*i

        if 0<=rr<4 and 0<=cc<4 and loc[fish[rr][cc][0]][2]:
            loc[fish[rr][cc][0]][2] = 0
            fish[rr][cc][0], fish[r][c][0] = fish[r][c][0], fish[rr][cc][0]
            print(f'현재까지 물고기: {total+fish[r][c][0]}')
            shark(rr, cc, fish[rr][cc][1], total+fish[r][c][0])
            fish[rr][cc][0], fish[r][c][0] = fish[r][c][0], fish[rr][cc][0]
            loc[fish[rr][cc][0]][2] = 1

def move_fish():    #물고기 이동
    for i in range(1, 17):
        if not loc[i][2]:
            continue

        r, c = loc[i][0], loc[i][1]
        direction = fish[r][c][1]
        print(f'r, c: {r,c}')

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

start = fish[0][0][0]
fish[0][0][0] = 0
loc[start][2] = 0

# shark(0, 0, fish[0][0][1], start)

shark(0, 0, fish[0][0][1], start)
print(ans)