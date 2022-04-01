from collections import deque

def bfs():
    queue = deque([(N, 0)])

    while queue:
        n, d = queue.popleft()

        for i in ['+1', '-1', '*2', '-10']:
            rlt = eval(str(n) + i)
            if rlt <= 0:
                continue

            queue.append((rlt, d + 1))

            if rlt == M:
                return d + 1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    print(bfs())
