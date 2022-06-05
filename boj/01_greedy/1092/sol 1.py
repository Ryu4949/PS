import sys
input = sys.stdin.readline

N = int(input())
cranes = [*map(int, input().split())]
M = int(input())
boxes = [*map(int, input().split())]

cranes.sort(reverse=True)
boxes.sort(reverse=True)

cnt = [0] * N
visited = [False] * M
total = 0

if boxes[0] > cranes[0]:
    print(-1)
else:
    c = 0
    b = 0
    while total != M:
        if not visited[b] and cranes[c] >= boxes[b]:
            cnt[c] += 1
            visited[b] = True
            total += 1
            c = (c+1)%N
            b = (b+1)%M
            if b == 0 or c == 0:
                b = 0
                c = 0
        else:
            b = (b+1)%M
            if b == 0:
                c = 0

    print(max(cnt))