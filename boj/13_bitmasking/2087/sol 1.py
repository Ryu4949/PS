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

left_sum.sort()
right_sum.sort()

for i in range(len(left_sum)):
    s = 0
    e = len(right_sum)-1
    while s <= e:
        mid = (s+e)//2
        if left_sum[i][0] + right_sum[mid][0] == K:
            print(bin(left_sum[i][1]+right_sum[mid][1])[2:].zfill(N)[::-1])
            exit()
        elif left_sum[i][0] + right_sum[mid][0] > K:
            e = mid-1
        else:
            s = mid+1
