from pprint import pprint

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]

visited = [False] * 17  #상어에게 먹힌 물고기 체크
fish = [[[] for _ in range(4)] for _ in range(4)]

for i in range(4):
    data = [*map(int, input().split())]
    for j in range(4):
        fish[i][j].append(data[2*j])
        fish[i][j].append(data[2*j+1]-1)
ans = 0
pprint(fish, width = 50)

def is_fish(r, c, d):   #상어가 이동할 수 있는 물고
    for p in range(1, 5):
        rr, cc = r+dr[d]*p, c+dc[d]*p
        if 0<=rr<4 and 0<=cc<4 and fish[rr][cc]:
            return True
    return False


def shark(r, c, d, total): #r, c는 상어의 위치, total은 먹은 물고기 총합
    if not is_fish(r, c, d):
        return

    

