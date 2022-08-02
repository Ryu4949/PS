N, S = map(int, input().split())
nums = [*map(int, input().split())]
ps = [0] * (N+1)

ps[1] = nums[0]
for i in range(2, N+1):
    ps[i] = ps[i-1] + nums[i-1]

i = 0
j = 1
min_length = N+1

while i < j and j <= N:
    prefix_sum = ps[j]-ps[i]
    if prefix_sum >= S:
        min_length = min(min_length, j-i)
        i += 1
    else:
        j += 1

print(min_length if min_length < N+1 else 0)