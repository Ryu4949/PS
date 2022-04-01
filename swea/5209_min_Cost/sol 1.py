def cost(i):
    global costs, ans

    if costs > ans: #비용이 기존의 최소비용을 넘어선다면 중단
        return

    if i == N:  #마지막 작업까지 확인하고나면 ans를 갱신
        ans = costs
        return

    for j in range(N):
        if not visited[j]:  #아직 처리하지 않은 일 중에서
            costs += arr[i][j]  #비용에 더해주고, 처리한 일에 방문처리하고 다음단계
            visited[j] = True
            cost(i+1)
            costs -= arr[i][j]  #원상복구
            visited[j] = False

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[*map(int, input().split())] for _ in range(N)]
    visited = [False] * N

    costs = 0
    ans = 1500

    cost(0)

    print(f'#{tc} {ans}')