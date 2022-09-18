chess = [1, 1, 2, 2, 2, 8]
pieces = [*map(int, input().split())]
ans = [0] * 6

for i in range(6):
    ans[i] = chess[i] - pieces[i]

print(*ans)