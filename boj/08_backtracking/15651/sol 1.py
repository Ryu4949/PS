N, M = map(int, input().split())
num_list = list(range(1, N+1))
rlt = []

def perm(i):
    if i == M:
        print(*rlt)
        return

    for j in range(1, N+1):
        rlt.append(j)
        perm(i+1)
        rlt.pop()

perm(0)