t = int(input())
for num in range(1, t+1):
    k, n, m = map(int, input().split())
    charge = list(map(int, input().split()))
    
    #출발점~충전소~종점 사이의 거리를 저장
    distance = [0] * (m + 1)
    for i in range(len(distance)):
        if i == 0:
            distance[i] = charge[0]
        elif i == len(distance)-1:
            distance[i] = n - charge[-1]
        else:
            distance[i] = charge[i] - charge[i-1]
    
    #cnt는 충전횟수, i는 인덱스, stops는 충전한 이후로 이동한 정류장 수를 저장
    cnt = 0
    i = 0
    stops = 0
    
    while i < len(distance):
        #충전소간 거리가 최대 이동 가능 정류장보다 크다면 cnt를 0으로 바꾸고 종료
        if distance[i] > k:
            cnt = 0
            break
            
        #현재까지 이동한 충전소와 다음 충전소까지의 거리의 합이 최대 이동 가능 정류장보다 크다면
        #충전횟수 +1, 이동한 정류장을 초기화한 후에 다시 거리를 더해줌
        elif stops + distance[i] > k:
            stops = 0
            cnt += 1
            stops += distance[i]
        
        #다음 충전소까지 이동해도 최대 이동 가능 정류장보다 작으면 그냥 그 거리만큼 더해줌
        else:
            stops += distance[i]

        i += 1

    print(f'#{num} {cnt}')