from collections import Counter

N, M = map(int, input().split())
nums = [*map(int, input().split())]
ps = [0] * (N+1)
for i in range(1, N+1):
    ps[i] = (nums[i-1]+ps[i-1])%M

cnt = Counter(ps[1:])
ans = 0

for key, value in cnt.items():
    if key:
        ans += value*(value-1)//2
    else:
        ans += value*(value-1)//2 + value

print(ans)