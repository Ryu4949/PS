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
for _ in range(M):
    a, b = map(int, input().split())

    if parent[a] != parent[b]:
        union(a, b)

for i in range(1, N+1):
    find(i)

lectures = [*map(int, input().split())]
cnt = 0
for i in range(1, N):
    if parent[lectures[i]] != parent[lectures[i-1]]:
        cnt += 1

print(cnt)