import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst = list(set(lst))
lst.sort()
rlt = []

def perm(i):
    if i == M:
        print(*rlt)
        return

    for j in lst:
        rlt.append(j)
        perm(i+1)
        rlt.pop()

perm(0)

