def count_blueray(length, array):
    cnt = 1
    lecture = 0
    for i in range(len(array)):
        if lecture + array[i] > length:
            lecture = 0
            lecture += array[i]
            cnt += 1
        else:
            lecture += array[i]
    return cnt

N, M = map(int, input().split())
guitar = list(map(int, input().split()))

start = max(guitar)
end = sum(guitar)

ans = 0
while start <= end:
    mid = (start + end) // 2
    if count_blueray(mid, guitar) > M:
        start = mid + 1
    else:
        ans = mid
        end = mid - 1

print(ans)