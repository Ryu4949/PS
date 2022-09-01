N = int(input())
nums = [*map(int, input().split())]
nums = list(set(nums))
nums.sort()
print(*nums)