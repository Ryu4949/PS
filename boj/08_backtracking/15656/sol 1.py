import sys

N, M = map(int, input().split())
lst = list(map(int, sys.stdin.readline().split()))
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
