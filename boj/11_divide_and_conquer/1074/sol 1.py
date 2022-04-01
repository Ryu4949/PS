#pypy는 메모리 초과
N, R, C = map(int, input().split())

def make_z(r, c, size):
    global cnt

    if size == 2:
        for i in range(r, r+size):
            for j in range(c, c+size):
                cnt += 1
                if i == R and j == C:
                    return

    half = size // 2
    move = (size ** 2) // 4
    if R < r+half and C < c+half:
        make_z(r, c, half)
    elif R < r+half and C >= c+half:
        cnt += move
        make_z(r, c+half, half)
    elif R >= r+half and C < c+half:
        cnt += move*2
        make_z(r+half, c, half)
    else:
        cnt += move*3
        make_z(r+half, c+half, half)

cnt = 0
make_z(0, 0, 2**N)
print(cnt-1)