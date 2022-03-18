def cnt(w):
    cnt = 0
    m = 0
    for i in range(len(money)):
        if m < money[i]:
            cnt += 1
            m = w
            m -= money[i]
        else:
            m -= money[i]
    if cnt <= M:
        return True
    else:
        return False

N, M = map(int, input().split())
money = []
for _ in range(N):
    money.append(int(input()))

start = max(money)
end = sum(money)

ans = 0
while start <= end:
    mid = (start + end)//2
    if cnt(mid):
       ans = mid
       end = mid-1
    else:
        start = mid+1

print(ans)
