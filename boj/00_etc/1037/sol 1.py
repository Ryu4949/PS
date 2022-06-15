N = int(input())
nums = [*map(int, input().split())]
nums.sort()
print(nums[0] * nums[-1])