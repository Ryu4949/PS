#주석 처리된 부분으로 인해 print를 몇번이나 찍었는지 모르겠다
#deepcopy 중요!!


from pprint import pprint
import copy
def shark(sr, sc, direction, total):    #상어의 위치와 방향 그리고 총 먹은 양
    global fish, loc
    move_fish(sr, sc) #현재 상어의 위치를 기준으로 물고기가 이동한다

    target = search(sr, sc, direction) #target이라는 변수에 상어의 현재 위치에서 먹을 수 있는 물고기의 목록을 담음

    if not target:  #먹을 수 있는 물고기가 없다면 rlt에 현재까지 먹은 물고기 양의 합을 담고 종료한다
        rlt.append(total)
        return

    base_fish, base_loc = copy.deepcopy(fish), copy.deepcopy(loc)
    for i in target:    #만약 먹을 수 있는 물고기가 있다면 하나씩 확인
        fr, fc = i[0], i[1]
        fish[fr][fc][2] = -1    #먹을 물고기를 먹힘 처리하고
        # fish[sr][sc][1] = fish[fr][fc][1]   #상어의 방향 바꿔주고
        loc[fish[fr][fc][0]], loc[fish[sr][sc][0]] = loc[fish[sr][sc][0]], loc[fish[fr][fc][0]]
        fish[sr][sc], fish[fr][fc] = fish[fr][fc], fish[sr][sc] #먹을 물고기와 상어의 위치를 바꾸고

        shark(fr, fc, fish[sr][sc][1], total+fish[sr][sc][0])   #다음단계 진행
        # print('**********************************')
        # print('원상복구 전')
        # pprint(fish)
        # print(loc)
        #
        # fish[sr][sc], fish[fr][fc] = fish[fr][fc], fish[sr][sc] #원상복구
        # # fish[sr][sc][1] = direction
        # fish[fr][fc][2] = 0
        # loc[fish[fr][fc][0]], loc[fish[sr][sc][0]] = loc[fish[sr][sc][0]], loc[fish[fr][fc][0]]
        # print('원상복구 잘 됐나?')
        # pprint(fish)
        # print(loc)
        # print('***************************************')
        fish = base_fish
        loc = base_loc

def move_fish(sr, sc):  #상어 위치를 인자로 받자
    for i in range(1, 17): #1~16번 물고기 이동
        r, c = loc[i][0], loc[i][1] #해당 번호의 물고기가 이미 먹힌 물고기면 pass
        if fish[r][c][2] == -1:
            continue

        direction = fish[r][c][1]

        for _ in range(9):
            rr, cc = r+dr[direction], c+dc[direction]

            if 0<=rr<4 and 0<=cc<4:
                if rr != sr or cc != sc: #방향대로 이동했을 때 범위 내이면서 상어가 있는 위치가 아니라면
                    fish[r][c][1] = direction
                    loc[fish[r][c][0]], loc[fish[rr][cc][0]] = loc[fish[rr][cc][0]], loc[fish[r][c][0]]
                    fish[r][c], fish[rr][cc] = fish[rr][cc], fish[r][c]
                    break

            direction = (direction+1)%8 #다음 위치가 범위 밖이거나 상어가 있는 곳이라면 방향 45도 회전하고 다시 확인

def search(sr, sc, direction):  # 현재 상어의 위치를 인자로 받는다
    target = []
    for p in range(1, 4):
        srr, scc = sr + dr[direction] * p, sc + dc[direction] * p

        if 0 <= srr < 4 and 0 <= scc < 4 and fish[srr][scc][2] == 0:  # 이동후 위치가 범위 내이면서 아직 안먹힌 물고기가 있으면
            target.append((srr, scc))  # 그 좌표 담아주기
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
print(rlt)
