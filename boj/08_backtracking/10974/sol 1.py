N = int(input())
lst = list(range(1, N+1))
rlt = []

def perm(i):
    if i == N:
        print(*rlt)

    for j in lst:
        if j not in rlt:
            rlt.append(j)
            perm(i+1)
            rlt.pop()

perm(0)
