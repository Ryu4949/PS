board = []

for _ in range(9):
    nums = list(map(int, input().split()))
    board.append(nums)

max_num = -1
max_idx = [0, 0]

for i in range(9):
    for j in range(9):
        if board[i][j] > max_num:
            max_num = board[i][j]
            max_idx = [i+1, j+1]

print(max_num)
print(*max_idx)