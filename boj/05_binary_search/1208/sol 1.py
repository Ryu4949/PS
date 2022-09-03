from itertools import combinations
import sys
input = sys.stdin.readline

N, S = map(int, input().split())
nums = [*map(int, input().split())]

left = nums[:N//2]
right = nums[N//2:]

L = len(left)
R = len(right)

sum_left = []
sum_right = []

for i in range(L+1):
    comb = combinations(left, i)
    for c in comb:
        sum_left.append(sum(c))

for i in range(R+1):
    comb = combinations(right, i)
    for c in comb:
        sum_right.append(sum(c))

sum_left.sort()
sum_right.sort()

cnt = 0
l = 0
r = len(sum_right)-1

while True:
    tmp = sum_left[l] + sum_right[r]
    if tmp > S:
        r -= 1
    elif tmp < S:
        l += 1
    else:
        sl = 1
        sr = 1
        ll = l+1
        rr = r-1
        while ll < len(sum_left) and sum_left[l] == sum_left[ll]:
            sl += 1
            ll += 1

        while rr >= 0 and sum_right[r] == sum_right[rr]:
            sr += 1
            rr -= 1

        cnt += sl*sr
        l = ll
        r = rr

    if l >= len(sum_left) or r < 0:
        break

print(cnt if S else cnt-1)