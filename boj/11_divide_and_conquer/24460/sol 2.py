def second_min(i, j):
    nums = []
    for r in range(i, i+2):
        for c in range(j, j+2):
            nums.append(chairs[r][c])
    nums.sort()
    return nums[1]

def choose(i, j, size):
    if size == 1:
        return chairs[0][0]

    if size == 2:
        return second_min(i, j)

    result = []
    half = size // 2

    for m in range(2):
        for n in range(2):
            result.append(choose(i+half*m, j+half*n, half))
    result.sort()
    return result[1]

N = int(input())
chairs = [list(map(int, input().split())) for _ in range(N)]

print(choose(0, 0, N))