N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))
d = [1] * N

for i in range(1, N):
    for j in range(i):
        if nums[j] < nums[i]:
            d[i] = max(d[i], d[j] + 1)

print(N-max(d))