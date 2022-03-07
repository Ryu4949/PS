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
        #중복되면 안되니까 없는 경우에만
        if j not in rlt:
            rlt.append(j)
            perm(i+1)
            rlt.pop()

perm(0)
