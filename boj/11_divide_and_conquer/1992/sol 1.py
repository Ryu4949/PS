def check(r, c, size):
    base = quad[r][c]
    for i in range(r, r+size):
        for j in range(c, c+size):
            if quad[i][j] != base:
                return False
    return True

def div(r, c, size):
    if check(r, c, size):
        print(quad[r][c], end='')
        return

    half = size // 2
    print('(', end='')
    for m in range(2):
        for n in range(2):
            div(r+half*m, c+half*n, half)
    print(')', end='')

N = int(input())
quad = [list(input()) for _ in range(N)]

div(0, 0, N)