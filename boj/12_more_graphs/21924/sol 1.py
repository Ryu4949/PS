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
parent = [i for i in range(N+1)]
edges = [[*map(int, input().split())] for _ in range(M)]
edges.sort(key=lambda x: x[2])

total = 0
costs = 0
for i in edges:
    total += i[2]
    if find(i[0]) != find(i[1]):
        union(i[0], i[1])
        costs += i[2]

for i in range(1, N):
    if find(i) != find(i+1):
        print(-1)
        break
else:
    print(total-costs)