import sys
input = sys.stdin.readline

N = int(input())
nums = [*map(int, input().split())]
S = int(input())
cnt = S

start = 0
temp_max = 0
temp_idx = 0
while cnt > 0:
    for i in range(start, N):
        if i - start > cnt:
            break

        if nums[i] > temp_max:
            temp_max = nums[i]
            temp_idx = i

    for i in range(temp_idx, start, -1):
        nums[i], nums[i-1] = nums[i-1], nums[i]

    cnt -= (temp_idx - start)
    start += 1
    if start >= N-1:
        break
    temp_max = nums[start]
    temp_idx = start



print(*nums)