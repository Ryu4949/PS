from itertools import combinations

def attack(archer): #특정 위치의 궁수가 공격하는 적의 위치
    atk = []
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                dist = abs(i-archer[0])+abs(j-archer[1])
                if dist <= D:
                    atk.append((dist, i, j))
    atk.sort(key=lambda x: (x[0], x[2]))
    if atk: #공격 대상이 있으면 거리-열 순으로 정렬해서 맨 처음 적 return
        return atk[0]
    else:   #조건에 맞는 적이 없으면 False
        return False

def is_enemy(): #남은 적이 있는지 확인. 한명이라도 남은 적이 있으면 True, 모두 빈칸이면 False
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                return True
    return False

def move(): #적들 이동시키는 함수
    for i in range(N-1, -1, -1):    #마지막 행부터 시작
        for j in range(M):
            if graph[i][j] == 1:    #해당 칸에 적이 있을 때
                if i == N-1:    #현재 마지막 행이라면 현재 위치만 0으로 바꾸고 끝
                    graph[i][j] = 0
                else:   #마지막 행이 아니면 바로 아래행 같은 열로 적이동시키고 지금 위치는 0으로
                    graph[i+1][j] = 1
                    graph[i][j] = 0


N, M, D = map(int, input().split())
castle = [[*map(int, input().split())] for _ in range(N)]
archers = [(N, i) for i in range(M)]    #궁수들이 있을 수 있는 위치들
archers_list = list(combinations(archers, 3))   #가능한 궁수들의 조합
ans = 0

for k in archers_list:
    graph = [castle[i][:] for i in range(N)]
    cnt = 0 #공격한 적의 수

    while True:
        if not is_enemy():  #적이 남아있지 않으면
            ans = max(ans, cnt) #최대값 갱신하고 종료
            break

        enemies = []    #이번에 공격할 적들
        for archer in k:
            target = attack(archer)
            if target:  #공격 대상이 있으면 enemies에 추가
                enemies.append(attack(archer))

        if enemies: #공격대상인 적들이 있으면
            for enemy in enemies:
                if graph[enemy[1]][enemy[2]] == 1:  #아직 공격하지 않은 적이면
                    cnt += 1    #cnt1 늘리고
                    graph[enemy[1]][enemy[2]] = 0   #그 위치는 0으로

        move()  #적들 이동

print(ans)
