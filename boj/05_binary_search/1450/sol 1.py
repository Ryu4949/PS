from itertools import combinations
import sys
input = sys.stdin.readline

N, C = map(int, input().split())
things = [*map(int, input().split())]

left = things[:N//2]
right = things[N//2:]

left_sum = []
right_sum = []

for i in range(len(left)+1):
    combs = combinations(left, i)
    for comb in combs:
        left_sum.append(sum(comb))

for i in range(len(right)+1):
    combs = combinations(right, i)
    for comb in combs:
        right_sum.append(sum(comb))

left_sum.sort()
right_sum.sort()

cnt = 0

for i in range(len(left_sum)):
    s = 0
    e = len(right_sum)-1
    part = left_sum[i]

    while s <= e:
        mid = (s+e)//2
        if right_sum[mid] + part <= C:
            s = mid+1
        else:
            e = mid-1
    cnt += e+1

print(cnt)