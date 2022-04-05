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
parent = [i for i in range(N)]
stars = [list(map(float, input().split())) for _ in range(N)]
edges = []

for i in range(N-1):
    for j in range(i+1, N):
        dist = (((stars[i][0] - stars[j][0])**2 + (stars[i][1] - stars[j][1])**2)**(1/2))
        edges.append((dist, i, j))

edges.sort()

ans = 0
for i in edges:
    if find(i[1]) != find(i[2]):
        union(i[1], i[2])
        ans += i[0]

print(f'{ans:.2f}')