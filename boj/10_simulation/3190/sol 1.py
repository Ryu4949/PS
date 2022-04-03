from collections import deque

#0은 빈칸, 1은 뱀, 2는 사과
N = int(input())
snake = [[0] * N for _ in range(N)]
K = int(input())
apple = []
for _ in range(K):
    a, b = map(int, input().split())
    apple.append((a-1, b-1))
L = int(input())
move = deque()
for _ in range(L):
    move.append(list(input().split()))

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

snake[0][0] = 1
for r, c in apple:
    snake[r][c] = 2

queue = deque([(0, 0)]) #뱀의 머리~꼬리 좌표
time = 0    #시간
direction = 0   #방향. 우-하-좌-상 순이기 때문에 0은 오른쪽으로 이동함을 가리킴
r = 0   #r, c는 최초의 좌표
c = 0

while True:
    time += 1   #시간 1 늘려주고

    rr = r+dr[direction]    #현재 방향대로 이동한 다음 좌표 계산
    cc = c+dc[direction]

    if 0<=rr<N and 0<=cc<N: #만약 범위 내라면 계속
        if snake[rr][cc] == 0:  #다음칸이 빈칸이면
            x, y = queue.popleft()  #뱀 몸통에서 꼬리를 빼서
            snake[x][y] = 0 #해당 좌표 0으로 만들고
            queue.append((rr, cc))  #이동한 곳을 뱀 몸통에 추가
            snake[rr][cc] = 1   #뱀이 있음을 표시
        elif snake[rr][cc] == 2:    #만약 다음칸에 사과가 있다면
            snake[rr][cc] = 1   #몸만 늘어나니까 그 칸 사과 없애고 뱀으로 바꿔주고
            queue.append((rr, cc))  #다음칸도 뱀의 몸통에 추가
        else:   #만약 다음칸이 뱀의 몸통의 일부라면 게임 끝
            break
    else:   #벽에 부딪히면 게임 끝
        break

    r, c = rr, cc   #좌표 r, c를 현재 위치로 바꿔줌

    if move and time == int(move[0][0]):    #방향전환 정보가 있는 큐에 원소가 있고, 현재 시간에 해당하는 것이 있다면
        if move[0][1] == 'D':   #방향전환이 D라면 현재 방향에서 오른쪽으로 전환
            direction = (direction+1)%4
        else:   #L이라면 현재 방향에서 왼쪽으로
            direction = (direction+3)%4
        move.popleft()  #move에서 처리한 방향전환은 제거

print(time)