def max_prob(i):
    global prob, ans

    if prob < ans:  #확률이 기존의 최대확률보다 낮으면 이후로는 더 높아질 수 없으므로 중단
        return

    if i == N:
        ans = prob
        return

    for j in range(N):
        #확률이 하나라도 0이면 최대값이 될 수 없으므로 이부분 제외하고 탐색
        #설령 모든 확률이 0이라도 초기 ans값이 0이므로 그때는 0을 출력가능
        if not visited[j] and arr[i][j] != 0:
            prob *= arr[i][j]   #확률 곱해주고
            visited[j] = True   #방문처리하고
            max_prob(i+1)       #다음단계 진행
            prob /= arr[i][j]   #원상복구
            visited[j] = False

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[*map(int, input().split())] for _ in range(N)]
    visited = [False] * N

    for i in range(N):
        for j in range(N):
            arr[i][j] /= 100

    prob = 1
    ans = 0

    max_prob(0)

    print(f'#{tc} {round(ans*100, 6):.6f}')