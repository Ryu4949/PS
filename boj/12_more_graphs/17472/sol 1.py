from collections import deque
def end_to_end(x, y):   #잡은 두 좌표 사이에 다른 땅이 없는지 체크
    x1, y1, x2, y2 = x[0], x[1], y[0], y[1]
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1

    check = 0
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            check += graph[i][j]

    if check == 2:  #두 좌표 사이의 graph값을 더해서 딱 2면 둘 사이에 다른 땅은 없는 것
        return True
    else:
        return False

def bfs(r, c):  #bfs 섬의 개수와 영역을 확인하는 용도
    queue = deque([(r, c)])
    visited[r][c] = True
    area = [(r, c)] #섬의 영역을 따로 담아준다

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            rr, cc = r+dr[i], c+dc[i]

            if 0<=rr<N and 0<=cc<M and not visited[rr][cc] and graph[rr][cc]:
                visited[rr][cc] = True
                queue.append((rr, cc))
                area.append((rr, cc))
    islands.append(area)

def find_bridge(a, b):  #두 섬을 연결하는 최소 다리길이 찾기
    length = 11 #초기값은 11(N, M의 최대값이 10이니까)
    for i in islands[a]:
        for j in islands[b]:    #두 섬에서 좌표 하나씩 잡아서 확인
            #잡은 두 좌표 행이든 열이든 하나는 같아야 가로든 세로든 연결 가능
            #그리고 잡은 두 좌표 사이에 다른 땅이 없어야 하고
            #다리의 길이는 최소 2이상이어야 함
            if (i[0] == j[0] or i[1] == j[1]) and end_to_end(i, j) and abs(i[0]-j[0]) + abs(i[1]-j[1])-1 >= 2:
                length = min(length, abs(i[0]-j[0]) + abs(i[1]-j[1])-1) #위 조건 만족하면 최소값 갱신
    return length

def find(x):    #find 함수
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):    #union 함수
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N, M = map(int, input().split())
graph = [[*map(int, input().split())] for _ in range(N)]
visited = [[False] * M for _ in range(N)]
islands = []

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

island = 0  #섬 몇개?
for i in range(N):
    for j in range(M):
        if graph[i][j] and not visited[i][j]:
            bfs(i, j)
            island += 1

bridges = []    #두 섬을 연결하는 다리가 있는 경우 (섬1, 섬2, 다리길이) 이렇게 담아줌
for i in range(island-1):
    for j in range(i+1, island):
        bridge = find_bridge(i, j)
        if bridge != 11:
            bridges.append((i, j, bridge))

bridges.sort(key=lambda x: x[2])    #다리 길이 오름차순 정렬

ans = 0
parent = [i for i in range(island)]

for i in bridges:   #MST
    if find(i[0]) != find(i[1]):
        union(i[0], i[1])
        ans += i[2]

for i in range(island-1):
    if find(i) != find(i+1):    #모든 섬이 하나로 연결되지 않았다면 -1
        print(-1)
        break
else:
    print(ans)

