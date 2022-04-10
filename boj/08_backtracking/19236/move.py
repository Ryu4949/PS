def move_fish(sr, sc):  #상어 위치를 인자로 받자
    for i in range(1, 17): #1~16번 물고기 이동
        r, c = loc[i][0], loc[i][1] #해당 번호의 물고기가 이미 먹힌 물고기면 pass
        if fish[r][c][2] == -1:
            continue

        direction = fish[r][c][1]

        for _ in range(9):
            rr, cc = r+dr[direction], c+dc[direction]

            if 0<=rr<4 and 0<=cc<4 and (rr != sr or cc != sc): #방향대로 이동했을 때 범위 내이면서 상어가 있는 위치가 아니라면
                loc[fish[r][c][0]], loc[fish[rr][cc][0]] = loc[fish[rr][cc][0]], loc[fish[r][c][0]]
                fish[r][c], fish[rr][cc] = fish[rr][cc], fish[r][c]
                break

            direction = (direction+1)%8 #다음 위치가 범위 밖이거나 상어가 있는 곳이라면 방향 45도 회전하고 다시 확인
