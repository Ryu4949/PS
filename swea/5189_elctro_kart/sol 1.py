#시작점은 0으로 정해져있고 모든 순열을 확인
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * N
    rlt = []

    #i: 몇개의 구역을 고려했는지, l: 직전 출발점, s: 그때까지의 배터리 소비량 합계
    def perm(i, l, s):
        #i == N이면 모든 구역을 방문했다는 의미이므로, 다시 출발점으로 돌아가는데 드는 배터리 소비량을 더해주고
        #rlt에 추가
        if i == N:
            rlt.append(s+graph[l][0])
            return

        #0은 출발점이니까 제외
        #1~N-1까지 방문하지 않은 곳에 대해
        for j in range(1, N):
            if not visited[j]:
                #방문처리하고, 다음단계로 보내고
                visited[j] = True
                perm(i+1, j, s+graph[l][j])
                #원상복구
                visited[j] = False

    perm(1, 0, 0)

    print(f'#{tc} {min(rlt)}')