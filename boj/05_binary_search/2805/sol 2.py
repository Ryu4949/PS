N, M = map(int, input().split())
wood = list(map(int, input().split()))

start = 0
end = max(wood)

h = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for i in wood:
        total += max(i-mid, 0)
    if total >= M:
        h = mid
        start = mid + 1
    else:
        end = mid - 1


print(h)
