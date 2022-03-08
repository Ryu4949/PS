import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
rlt = []
visited = [False] * N

def perm(i):
    for j in range(len(rlt)-1):
        if rlt[j+1] < rlt[j]:
            return

    if i == M:
        print(*rlt)
        return

    last = 0
    for j in range(N):
        if not visited[j] and last != lst[j]:
            rlt.append(lst[j])
            visited[j] = True
            last = lst[j]
            perm(i+1)
            rlt.pop()
            visited[j] = False

perm(0)