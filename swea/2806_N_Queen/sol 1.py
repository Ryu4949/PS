T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = 0

    queen = [0] * N
    visited = [False] * N

    def is_promising(depth):
        for j in range(depth):
            if abs(queen[depth]-queen[j]) == depth-j:
                return False
        return True

    def dfs(i):
        global cnt

        if i == N:
            cnt += 1
            return

        else:
            for j in range(N):
                if not visited[j]:
                    queen[i] = j
                    visited[j] = True

                    if is_promising(i):
                        dfs(i+1)
                    visited[j] = False

    dfs(0)
    print(f'#{tc} {cnt}')