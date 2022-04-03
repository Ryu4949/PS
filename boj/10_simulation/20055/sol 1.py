from collections import deque

N, K = map(int, input().split())
dur = [*map(int, input().split())]
belt = deque()
for i in dur:
    belt.append([0, i]) #0번 인덱스는 로봇이 있는지 없는지(있으면 1), 1번 인덱스는 내구도

step = 0    #단계
up = 0  #올리는 위치
down = N-1  #내리는 위치
while True:
    step += 1

    #벨트가 전체 회전한다
    belt.appendleft(belt.pop())

    #내리는 위치에 로봇이 있으면 내린다
    if belt[down][0] == 1:
        belt[down][0] -= 1

    #로봇들이 다음칸으로 이동할 수 있으면 이동한다.
    #이때 다음칸이 내리는 위치면 내리도록 해주고
    #이동할 수 있는 경우는 다음칸에 로봇이 없으면서 내구도가 1 이상이어야 함
    for i in range(down-1, -1, -1):
        if belt[i][0] == 1 and belt[i+1][0] == 0 and belt[i+1][1] >= 1: #이동가능하면
            belt[i][0] -= 1 #원래 위치의 로봇을 빼서
            belt[i+1][0] += 1   #다음 위치로 옮겨주고
            belt[i+1][1] -= 1   #옮긴 위치의 내구도 -1

            if i+1 == down: #옮겼는데 내리는 위치면
                belt[i+1][0] -= 1   #내린다

    #로봇을 올린다
    if belt[up][1] >= 1:    #올리는 위치의 내구도가 1 이상이면
        belt[up][0] += 1    #올려주고
        belt[up][1] -= 1    #내구도는 -1

    cnt = 0 #내구도가 0인 칸의 개수
    for i in belt:
        if i[1] <= 0:
            cnt += 1

    if cnt >= K:    #내구도 0인 칸이 K개 이상이면 끝
        break

print(step)
