N = int(input())
cnt = 0
queen = [0] * N

def is_promising(depth):
    for j in range(depth):
        if queen[depth] == queen[j] or abs(queen[depth]-queen[j]) == depth-j:
            return False
    return True

def dfs(i):
    global cnt

    if i == N:
        cnt += 1
        return

    else:
        for j in range(N):
            queen[i] = j
            if is_promising(i):
                dfs(i+1)

dfs(0)
print(cnt)