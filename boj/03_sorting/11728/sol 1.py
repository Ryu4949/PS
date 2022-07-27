N, M = map(int, input().split())
nums = [*map(int, input().split())] + [*map(int, input().split())]
nums.sort()
print(*nums)