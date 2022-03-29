def dfs():
    # 행, 열, 수의 합계
    stack = [(0, 0, graph[0][0])]

    while stack:
        r, c, v = stack.pop()

        for i in range(2):
            rr, cc = r + dr[i], c + dc[i]

            # 범위 내일 경우
            if 0 <= rr < N and 0 <= cc < N:
                # 목적지이면 rlt에 그때까지의 합계를 rlt에 추가
                if rr == N - 1 and cc == N - 1:
                    rlt.append(v + graph[rr][cc])
                # 목적지가 아닌 경우 수의 합을 갱신해주고 다음 위치를 스택에 push
                else:
                    stack.append((rr, cc, v + graph[rr][cc]))

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]

    dr = [1, 0]
    dc = [0, 1]

    #목적지에 도달했을 때 그때까지의 합계를 담을 리스트
    rlt = []

    dfs()

    #최소값 출력
    print(f'#{tc} {min(rlt)}')