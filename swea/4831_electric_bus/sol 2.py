    #DP
T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    big = 10000  #최소값을 구하는 문제니까 답이 될 수 없는 큰 수중 아무거나 설정
    memo = [big] * (N+1)    #memo 리스트
    charge = list(map(int, input().split()))    #충전소의 위치

    for i in range(K+1):    #초기값 설정은 출발점으로부터 K번 정류장까지를 0으로
        memo[i] = 0

    for i in charge:    #충전소의 위치를 앞에서부터 확인하면서
        for j in range(i+1, i+1+K): #충전소가 있으면 그 바로 다음 위치부터 K개의 정류장의 값을 충전소 위치의 값 + 1로 바꿔줌
            if j <= N and memo[i]+1 < memo[j]:  #그런데 바꿔줄 값이 기존에 저장되어 있던 값보다 작을 때만 바꿈
                memo[j] = memo[i] + 1

    # 중간에 충전을 하고도 도달하지 못하는 정류장이 있다면 그지점부터 종점까지는 값이 big이 됨
    # 그런 경우에는 종점에 도착하지 못하므로 0을 저장하고, 아니라면 마지막 정류장의 값을 저장
    rlt = memo[-1] if memo[-1] < big else 0
    print(memo)

    print(f'#{tc} {rlt}')
