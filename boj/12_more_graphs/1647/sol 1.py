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

N, M = map(int, input().split())
roads = [[*map(int, input().split())] for _ in range(M)]
roads.sort(key=lambda x: x[2])
parent = [i for i in range(N+1)]

ans = []
for i in roads:
    if find(i[0]) != find(i[1]):
        union(i[0], i[1])
        ans.append(i[2])

print(sum(ans)-max(ans))