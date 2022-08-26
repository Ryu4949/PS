L, P = map(int, input().split())
nums = [*map(int, input().split())]
gap = [0] * 5

for i in range(5):
    gap[i] = nums[i]-L*P

print(*gap)