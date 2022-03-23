def check(n):
    cnt = 0
    for i in drink:
        cnt += i // n
    return cnt

N, K = map(int, input().split())
drink = []
for _ in range(N):
    drink.append(int(input()))

start = 1
end = max(drink)

ans = 0
while start <= end:
    mid = (start + end) // 2
    if check(mid) >= K:
       ans = mid
       start = mid + 1
    else:
        end = mid - 1

print(ans)