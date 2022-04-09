import sys
input = sys.stdin.readline

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N = int(input())
graph = [[*map(int, input().split())] for _ in range(N)]
parent = [i for i in range(N)]
flow = []

for i in range(N):
    for j in range(i+1, N):
        flow.append((i, j, graph[i][j]))

flow.sort(key=lambda x: x[2])

ans = 0
for i in flow:
    if find(i[0]) != find(i[1]):
        union(i[0], i[1])
        ans += i[2]

print(ans)