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

while True:
    M, N = map(int, input().split())
    if M == 0 and N == 0:
        break
    parent = [i for i in range(M)]
    roads = [[*map(int, input().split())] for _ in range(N)]
    roads.sort(key=lambda x: x[2])

    save = 0
    total = 0
    for i in roads:
        total += i[2]
        if find(i[0]) != find(i[1]):
            union(i[0], i[1])
            save += i[2]

    print(total-save)