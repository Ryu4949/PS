def check(i, j):
    nums = [data[i][j], data[i+1][j], data[i][j+1], data[i+1][j+1]]
    nums.sort()
    return nums[-2]

def div(i, j, size):
    if size == 2:
        return(check(i, j))

    arr = []
    for m in range(2):
        for n in range(2):
            arr.append(div(i+(size//2)*m, j+(size//2)*n, size//2))

    arr.sort()
    return arr[-2]

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

print(div(0, 0, N))

