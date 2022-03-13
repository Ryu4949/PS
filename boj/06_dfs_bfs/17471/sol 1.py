N = int(input())
pop = list(map(int, input().split()))

#연결된 도시는 1로 표시
connected = [[float('inf')] * N for _ in range(N)]
for i in range(N):
    nums = list(map(int, input().split()))
    for j in range(1, nums[0]+1):
        connected[i][nums[j]-1] = 1
        connected[nums[j]-1][i] = 1

#자기자신은 0
for i in range(N):
    for j in range(N):
        if i == j:
            connected[i][j] = 0

#선거구1과 2, 1에 우선 1번 도시를 넣고 시작함
ward_1 = [0]
ward_2 = []

#선거구 별 인구 차이를 담아줄 리스트
rlt = []
def dfs(i):
    if i == N:
        #빈선거구 있으면 X
        if not ward_2:
            return

        #선거구 내의 도시들이 연결되지 않은 경우가 있다면 X
        elif not check_connected(ward_1) or not check_connected(ward_2):
            return

        #선거구별로 최소 1개 구역이 있고, 각 선거구 내의 모든 도시가 서로 연결되었다면
        #인구의 차이를 rlt에 추가
        else:
            pop_1 = 0
            pop_2 = 0
            for j in ward_1:
                pop_1 += pop[j]

            for j in ward_2:
                pop_2 += pop[j]

            rlt.append(abs(pop_1 - pop_2))
            return

    ward_1.append(i)
    dfs(i+1)
    ward_1.pop()
    ward_2.append(i)
    dfs(i+1)
    ward_2.pop()

#각 선거구 내의 도시가 서로 연결되었는지 확인해주는 함수
def check_connected(arr):
    n = len(arr)
    #선거구 내의 구역으로 이루어진 새로운 리스트를 만들고
    connect = [[float('inf')] * n for _ in range(n)]

    #기본 정보는 맨 처음에 만든 connected에서 가져오고
    for i in range(n):
        for j in range(n):
            connect[i][j] = connected[arr[i]][arr[j]]

    #각 구역간 최단거리 갱신. 직접 연결되었든, 간접적으로 연결되었든 연결만 되어있다면 inf가 아닌 수가 저장돼있을 것
    for k in range(n):
        for i in range(n):
            for j in range(n):
                connect[i][j] = min(connect[i][j], connect[i][k] + connect[k][j])

    #확인하면서 inf가 하나라도 있다면 연결되지 않은 구역이 존재한다는 뜻이므로 False
    for i in range(n):
        for j in range(n):
            if connect[i][j] == float('inf'):
                return False
    return True

dfs(1)

if len(rlt) == 0:
    print(-1)
else:
    print(min(rlt))