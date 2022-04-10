def search(sr, sc, direction): #현재 상어의 위치를 인자로 받는다
    target = []
    for p in range(1, 4):
        srr, scc = sr+dr[direction]*p, sc+dc[direction]*p
        
        if 0<=srr<4 and 0<=scc<4 and fish[srr][scc][2] == 0:    #이동후 위치가 범위 내이면서 아직 안먹힌 물고기가 있으면
            target.append((srr, scc))   #그 좌표 담아주기
    return target

        