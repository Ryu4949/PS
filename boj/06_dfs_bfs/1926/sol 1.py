N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

#그림의 넓이를 담는 변수. 그림이 존재하는 영역에서만 카운트할 것이기 때문에 기본 값을 1로둔다
cnt = 1
picture = []

def dfs(r, c):
    global cnt
    stack = [(r, c)]

    if 0<=r<N and 0<=c<M and graph[r][c] == 1:
        graph[r][c] = 0
        while stack:
            r, c = stack.pop()

            for i in range(4):
                rr, cc = r+dr[i], c+dc[i]

                if 0<=rr<N and 0<=cc<M and graph[rr][cc] == 1 and not visited[r][c]:
                    cnt += 1
                    stack.append((rr, cc))
                    graph[rr][cc] = 0
                    
        #넓이를 다 카운트 했다면 리스트에 넣어주고 변수 초기화
        picture.append(cnt)
        cnt = 1

for i in range(N):
    for j in range(M):
        dfs(i, j)

#그림이 하나도 없는 경우
max_picture = max(picture) if len(picture) > 0 else 0

print(len(picture))
print(max_picture)