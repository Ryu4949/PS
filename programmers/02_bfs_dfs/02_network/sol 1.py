n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

def find(x, parent):
    if x != parent[x]:
        parent[x] = find(parent[x], parent)
    return parent[x]

def union(a, b, parent):
    a = find(a, parent)
    b = find(b, parent)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(n, computers):
    parent = [i for i in range(n)]
    for i in range(n):
        for j in range(n):
            if computers[i][j] and find(i, parent) != find(j, parent):
                union(i, j, parent)

    for i in range(n):
        find(i, parent)

    return len(set(parent))

print(solution(n, computers))