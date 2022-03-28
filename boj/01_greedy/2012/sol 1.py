N = int(input())
exp = [int(input()) for _ in range(N)]
exp.sort()

ans = 0
for i in range(N):
    ans += abs((i+1)-exp[i])

print(ans)