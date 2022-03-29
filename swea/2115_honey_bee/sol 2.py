##다른 풀이를 참고하였습니다

#주어진 영역에서 최대 수익을 반환하는 함수
def cal(row, start):
    rlt = 0
    for i in range(1, 1<<M):
        honey = 0
        profit = 0
        for j in range(M):
            if i&(1<<j):
                honey += graph[row][start+j]
                profit += graph[row][start+j] ** 2
        if honey <= C:
            rlt = max(rlt, profit)
    return rlt

T = int(input())
for tc in range(1, T + 1):
    N, M, C = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]

    arr = []
    for i in range(N):
        for j in range(N-M+1):
            arr.append((i, j, cal(i, j)))

    ans = 0
    for i in range(len(arr)-1):
        for j in range(i, len(arr)):
            if arr[i][0] == arr[j][0] and arr[i][1] + M - 1 >= arr[j][1]:
                continue
            ans = max(ans, arr[i][2] + arr[j][2])
    print(f'#{tc} {ans}')