K = int(input())
N = int(input())
Q = []
player = list(range(1, 9))
for _ in range(N):
    Q.append(list(input().split()))

bomb = 210

holder = K-1
time = 0
idx = 0
while True:
    #경과한 시간 더하고
    time += int(Q[idx][0])

    #시간이 폭탄 터지는 시간 이상이되면 그 때 들고있는 플레이어를 출력하고 종료
    if time >= 210:
        print(player[holder])
        break

    #시간이 아직 남았고, 문제를 맞혔다면 다음 플레이어에게 전달
    if Q[idx][1] == 'T':
        holder = (holder + 1) % 8

    #다음 질문으로
    idx += 1


