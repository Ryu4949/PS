T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()    #A를 정렬

    cnt = 0     #조건을 만족하는 개수
    for i in B:
        start = 0       #시작
        end = N - 1     #끝
        flag = None     #초기값은 없음, 0은 왼쪽구간 탐색을 의미하고 1은 오른쪽 구간 탐색을 의미
        while start <= end:
            mid = (start + end) // 2
            if A[mid] == i:     #찾는 값 찾았으면 cnt 1 늘려주고 종료
                cnt += 1
                break
            elif A[mid] > i:    #mid의 값이 찾는 값보다 크면 왼쪽 탐색
                end = mid - 1
                if flag == 0:   #그런데 직전에 이미 왼쪽 구간을 탐색했다면 조건을 만족하지 못하므로 중단
                    break
                else:           #직전에 오른쪽 구간을 탐색했다면 flag를 0으로 바꿔주고 왼쪽 탐색
                    flag = 0
            else:               #mid의 값이 찾는 값보다 작다면 오른쪽 구간 탐색
                start = mid + 1
                if flag == 1:   #직전에 오른쪽 구간을 탐색했다면 중단. 왼쪽을 탐색했었다면 flag 1로 바꿔주고 계속
                    break
                else:
                    flag = 1

    print(f'#{tc} {cnt}')