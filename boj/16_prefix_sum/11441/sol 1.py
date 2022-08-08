N = int(input())
nums = [*map(int, input().split())]
pre = [0] * (N+1)
pre[1] = nums[0]
for i in range(2, N+1):
    pre[i] = pre[i-1]+nums[i-1]
M = int(input())
for _ in range(M):
    s, e = map(int, input().split())
    print(pre[e]-pre[s-1])