from collections import deque

def bfs(r, c):
    queue = deque([(r, c, 1, board[r][c])])

    while queue:
        r, c, d, s = queue.popleft()

        for i in range(4):
            rr, cc = r + dr[i], c + dc[i]

            if 0 <= rr < 4 and 0 <= cc < 4:
                if d == 6:
                    lst.append(s + board[rr][cc])
                else:
                    queue.append((rr, cc, d + 1, s + board[rr][cc]))

T = int(input())
for tc in range(1, T+1):
    board = [list(input().split()) for _ in range(4)]
    lst = []

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for i in range(4):
        for j in range(4):
            bfs(i, j)

    print(f'#{tc} {len(set(lst))}')