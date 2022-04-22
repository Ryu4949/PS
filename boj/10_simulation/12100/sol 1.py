from pprint import pprint
from itertools import combinations

def up():
    for i in range(N):
        for j in range(N):
            r, c = i, j
            while True:
                if 0<=r-1<N and board[r][c] > 0:
                    if board[r-1][c] == 0 or board[r-1][c] == board[r][c]:
                        board[r-1][c] += board[r][c]
                        board[r][c] = 0
                        r -= 1
                    else:
                        break
                else:
                    break

def down():
    for i in range(N-1, -1, -1):
        for j in range(N):
            r, c = i, j
            while True:
                if 0<=r+1<N and board[r][c] > 0:
                    if board[r+1][c] == 0 or board[r+1][c] == board[r][c]:
                        board[r+1][c] += board[r][c]
                        board[r][c] = 0
                        r += 1
                    else:
                        break
                else:
                    break

def left():
    for j in range(N):
        for i in range(N):
            r, c = i, j
            while True:
                if 0<=c-1<N and board[r][c] > 0:
                    if board[r][c-1] == 0 or board[r][c-1] == board[r][c]:
                        board[r][c-1] += board[r][c]
                        board[r][c] = 0
                        c -= 1
                    else:
                        break
                else:
                    break

def right():
    for j in range(N-1, -1, -1):
        for i in range(N):
            r, c = i, j
            while True:
                if 0<=c+1<N and board[r][c] > 0:
                    if board[r][c+1] == 0 or board[r][c+1] == board[r][c]:
                        board[r][c+1] += board[r][c]
                        board[r][c] = 0
                        c += 1
                    else:
                        break
                else:
                    break

def find_max():
    max_val = 0
    for i in range(N):
        for j in range(N):
            max_val = max(max_val, board[i][j])
    return max_val
N = int(input())
board = [[*map(int, input().split())] for _ in range(N)]
directions = ['U', 'D', 'L', 'R']
order = list(combinations(directions*5, 5))

base = [arr[:] for arr in board]

ans = 0
for i in order:
    for j in i:
        if j == 'U':
            up()
        elif j == 'D':
            down()
        elif j == 'L':
            left()
        else:
            right()
    ans = max(ans, find_max())
    board = [arr[:] for arr in base]

print(ans)