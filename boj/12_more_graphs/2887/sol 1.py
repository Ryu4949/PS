import sys
input = sys.stdin.readline

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
planet = [[*map(int, input().split())] for _ in range(N)]
parent = [i for i in range(N)]
planet.sort(key=lambda x: (x[0], x[1], x[2]))

ans = 0
for i in range(N-1):
    for j in range(1, N):
        if set(planet[i]) & set(planet[j]):
            union(i, j)
            ans +=


print(ans)