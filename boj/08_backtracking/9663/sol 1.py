N = int(input())
board = [[0] * N for _ in range(N)]
cnt = 0

def is_promising(array):
    trans_array = list(zip(*array))

    for i in trans_array:
        if sum(i) > 1:
            return False

    lst = []
    for i in range(N):
        for j in range(N):
            if array[i][j] == 1:
                lst.append((i, j))

    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            if abs(lst[i][0]-lst[j][0]) == abs(lst[i][1]-lst[j][1]):
                return False
    return True

def dfs(i):
    global cnt

    if not is_promising(board):
        return

    if i == N:
        cnt += 1
        return

    for j in range(N):
        board[i][j] = 1
        dfs(i+1)
        board[i][j] = 0

dfs(0)

print(cnt)