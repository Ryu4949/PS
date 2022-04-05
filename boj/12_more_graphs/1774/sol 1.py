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

N, M = map(int, input().split())
parent = [i for i in range(N+1)]
loc = [[]]
edges = []

for _ in range(1, N+1):
    loc.append(list(map(int, input().split())))

for _ in range(M):
    a, b = map(int, input().split())
    union(a, b)

for i in range(1, N):
    for j in range(i+1, N+1):
        dist = ((loc[i][0]-loc[j][0])**2 + (loc[i][1]-loc[j][1])**2)**(1/2)
        edges.append((i, j, dist))

edges.sort(key=lambda x: x[2])

ans = 0
for i in edges:
    if find(i[0]) != find(i[1]):
        union(i[0], i[1])
        ans += i[2]

print(f'{ans:0.2f}')