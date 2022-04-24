from collections import defaultdict

N = int(input())
log = defaultdict(int)
ans = []

for _ in range(N):
    a, b = input().split()
    log[a] += 1

for i in log:
    if log[i]%2:
        ans.append(i)

ans.sort(reverse=True)

for i in ans:
    print(i)
