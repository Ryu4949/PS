def shark(sr, sc, direction, total):    #상어의 위치와 방향 그리고 총 먹은 양
    move_fish(sr, sc) #현재 상어의 위치를 기준으로 물고기가 이동한다

    target = search(sr, sc) #target이라는 변수에 상어의 현재 위치에서 먹을 수 있는 물고기의 목록을 담음

    if not target:  #먹을 수 있는 물고기가 없다면 rlt에 현재까지 먹은 물고기 양의 합을 담고 종료한다
        rlt.append(total)
        return

    for i in target:    #만약 먹을 수 있는 물고기가 있다면 하나씩 확인
        fr, fc = i[0], i[1]
        fish[fr][fc][2] = -1    #먹을 물고기를 먹힘 처리하고
        fish[sr][sc][1] = fish[fr][fc][1]   #상어의 방향 바꿔주고
        loc[fish[fr][fc][0]] = loc[0]
        fish[sr][sc], fish[fr][fc] = fish[fr][fc], fish[sr][sc] #먹을 물고기와 상어의 위치를 바꾸고
        shark(fr, fc, fish[fr][fc][1], total+fish[sr][sc][0])   #다음단계 진행
        fish[sr][sc], fish[fr][fc] = fish[fr][fc], fish[sr][sc] #원상복구
        fish[sr][sc][1] = direction
        fish[fr][fc][2] = 0
        loc[fish[fr][fc][0]] = loc[0]

