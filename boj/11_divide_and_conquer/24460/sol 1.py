import sys
sys.setrecursionlimit(10**6)

N = int(input())
chairs = [list(map(int, input().split())) for _ in range(N)]

def second_min(arr):
    nums = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            nums.append(arr[i][j])
    nums.sort()
    return nums[1]

def choose(arr):
    if len(arr) == 2:
        results.append(second_min(arr))
        return

    half = len(arr) // 2

    left_up = [arr[i][:half] for i in range(half)]
    right_up = [arr[i][half:] for i in range(half)]
    left_down = [arr[i][:half] for i in range(half, len(arr))]
    right_down = [arr[i][half:] for i in range(half, len(arr))]

    choose(left_down)
    choose(left_up)
    choose(right_down)
    choose(right_up)

    return

results = []
choose(chairs)
results.sort()

print(results[0]) if len(results) == 1 else print(results[1])

