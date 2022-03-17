def dfs(v):
    global cnt
    stack = [v]
    visited = [False] * N
    visited[v] = True

    while stack:
        v = stack.pop()

        if len(set(graph[v]) - {delete}) == 0:
            cnt += 1
            continue
        else:
            for i in graph[v]:
                if i != delete and not visited[i]:
                    stack.append(i)
                    visited[i] = True

N = int(input())
graph = [[] for _ in range(N)]
node = list(map(int, input().split()))

#그래프에 간선정보 추가하고, root 찾기
for i in range(N):
    if node[i] == -1:
        root = i
    else:
        graph[node[i]].append(i)

#delete는 삭제할 노드, cnt는 리프노드의 개수
delete = int(input())
cnt = 0

if delete == root:
    print(0)
else:
    dfs(root)
    print(cnt)