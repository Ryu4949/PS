import sys
input = sys.stdin.readline

def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b
N, M = map(int, input().split())
parent = [i for i in range(N)]
for turn in range(1, M+1):
    a, b = map(int, input().split())

    if find_parent(a) == find_parent(b):
        print(turn)
        break
    else:
        union(a, b)
else:
    print(0)