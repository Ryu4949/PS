import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

N = int(input())
nums = [*map(int, input().split())]
nums.sort()

cnt = 0
if N >= 3:
    for i in range(N-2):
        for j in range(i+1, N-1):
            base = nums[i]+nums[j]
            left = bisect_left(nums, -base, j+1)
            right = bisect_right(nums, -base, j+1)
            cnt += right-left

print(cnt)
