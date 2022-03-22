from pprint import pprint

N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b, c = map(int, input().split())
    tree[a].append((b, c))
    tree[b].append((a, c))

distance = [0] * (N+1)
def dfs(v):
    visited = [False] * (N+1)
    stack = [v]

    while stack:
        v = stack.pop()
        for i in tree[v]:
            if not visited[i[0]]:
                visited[i[0]] = True
                stack.append(i[0])
                distance[i[0]] = distance[v] + i[1]

dfs(1)
pprint(tree)
print(distance)

