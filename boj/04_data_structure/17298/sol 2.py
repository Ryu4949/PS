import sys
N = int(input())
data = list(map(int, sys.stdin.readline().split()))

stack = []
ans = [-1] * N

for i in range(N):
    while stack and data[stack[-1]] < data[i]:
        ans[stack.pop()] = data[i]
    stack.append(i)

print(*ans)