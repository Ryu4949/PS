N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

a = sorted(A)
b = sorted(B, reverse=True)

ans = 0
for i in range(N):
    ans += a[i] * b[i]

print(ans)