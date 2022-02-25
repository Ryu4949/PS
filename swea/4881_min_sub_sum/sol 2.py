T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * N   #첫행부터 밑으로 내려가는데 열이 겹치지 않아야 하므로, 이미 선택한 열인지 확인
    min_sum = 9999999   #최소값
    each_sum = 0    #백트래킹을 위한 부분합

    def sum_sub(i):
        global each_sum, min_sum
        #만약 부분합이 이미 최소값을 넘어선다면 중단하고 돌아감
        if each_sum > min_sum:
            return
        
        #마지막 행까지 선택을 완료했다면
        if i == N:
            #선택한 숫자들의 합과 현재의 최소값을 비교하고, 기존 최소값보다 작다면 교체
            if each_sum < min_sum:
                min_sum = each_sum
            return

        for j in range(N):
            #아직 사용하지 않은 열에 대해서 다음 단계 진행
            if not visited[j]:
                visited[j] = True   #이번에 선택한 열을 방문처리하고
                each_sum += data[i][j]  #해당 인덱스의 값을 더해주고
                sum_sub(i+1)    #다음 행 진행

                visited[j] = False  #그 후에 같은 행의 다음 열을 선택하는 경우를 위해 방문처리와 숫자합 복구
                each_sum -= data[i][j]

    sum_sub(0)
    print(f'#{tc} {min_sum}')