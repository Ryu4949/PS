from pprint import pprint
def cnt_honey(r, c):
    profit = 0
    honey = 0
    mp = 0
    visited = [False] * M

    def max_profit(i):
        nonlocal profit, honey, mp
        if honey > C:
            return

        if i == M:
            mp = max(mp, profit)
            return

        else:
            for j in range(M):
                if not visited[j]:
                    honey += graph[r][c + j]
                    profit += graph[r][c + j] ** 2
                    visited[j] = True
                    max_profit(i + 1)
                    honey -= graph[r][c + j]
                    profit -= graph[r][c + j] ** 2
                    visited[j] = False
                    max_profit(i + 1)

    max_profit(0)
    return mp

T = int(input())
for tc in range(1, T+1):
    N, M, C = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]

    loc = []
    for i in range(N):
        for j in range(N-M+1):
            loc.append([i, j, cnt_honey(i, j)])

    ans = 0
    for i in range(len(loc)-1):
        for j in range(i+1, len(loc)):
            if loc[i][0]==loc[j][0] and loc[i][1]+M-1 >= loc[j][1]:
                continue
            ans = max(ans, loc[i][2]+loc[j][2])
    print(f'#{tc} {ans}')
    # pprint(graph, width=50)
    # print(f'M: {M}, C: {C}')
    # pprint(loc)
    # print(ans)
    # print('-----------------------')