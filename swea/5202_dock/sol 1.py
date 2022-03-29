T = int(input())
for tc in range(1, T+1):
    N = int(input())
    time = [list(map(int, input().split())) for _ in range(N)]
    #끝나는 시간이 빠른 순서대로 정렬
    time.sort(key=lambda x: x[1])

    #cnt: 가능한 작업의 개수, end: 직전 작업이 끝난 시간
    cnt = 0
    end = 0
    for i in time:
        #새로운 작업의 시작시간이 직전 작업 종료시간 이후라면 작업 가능
        if i[0] >= end:

            #그때 cnt 1 늘려주고 작업 종료시간 갱신
            cnt += 1
            end = i[1]

    print(f'#{tc} {cnt}')