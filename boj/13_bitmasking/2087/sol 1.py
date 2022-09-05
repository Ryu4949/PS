N = int(input())
nums = [int(input()) for _ in range(N)]
K = int(input())

left = nums[:N//2]
right = nums[N//2:]

left_sum = []
right_sum = []

for i in range(1<<N//2):
    total = 0
    for j in range(N//2):
        if i & (1<<j):
            total += left[j]
    left_sum.append((total, i))

for i in range(1<<len(right)):
    total = 0
    for j in range(len(right)):
        if i & (1<<j):
            total += right[j]
    right_sum.append((total, i<<len(left)))

print(left_sum)
print(right_sum)