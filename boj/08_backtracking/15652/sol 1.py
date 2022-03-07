N, M = map(int, input().split())

rlt = []

def perm(i):
    for j in range(len(rlt)-1):
        if rlt[j+1] < rlt[j]:
            return

    if i == M:
        print(*rlt)
        return

    for j in range(1, N+1):
        rlt.append(j)
        perm(i+1)
        rlt.pop()

perm(0)
