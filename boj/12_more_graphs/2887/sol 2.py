def find(x):
    if parent[x] != x:
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
planet = []
for i in range(N):
    x, y, z = map(int, input().split())
    planet.append((x, y, z, i))

parent = [i for i in range(N)]
edges = []
for i in range(3):
    planet.sort(key = lambda x: x[i])
    for j in range(N-1):
        dist = min(abs(planet[j][0]-planet[j+1][0]), abs(planet[j][1]-planet[j+1][1]), abs(planet[j][2]-planet[j+1][2]))
        edges.append((dist, planet[j][3], planet[j+1][3]))

edges.sort()

ans = 0
for i in edges:
    if find(i[1]) != find(i[2]):
        union(i[1], i[2])
        ans += i[0]

print(ans)