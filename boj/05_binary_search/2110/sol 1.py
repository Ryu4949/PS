#gap이 주어질 때 그 gap 이상을 유지하면서 설치할 수 있는 공유기의 개수
def count_wifi(gap, array):
    cnt = 1
    idx = 0
    for i in range(1, len(array)):
        if array[i] - array[idx] >= gap:
            cnt += 1
            idx = i

    return cnt

N, C = map(int, input().split())
house = [int(input()) for _ in range(N)]
house.sort()

start = 1
end = house[-1] - house[0]

ans = 0
while start <= end:
    mid = (start + end) // 2
    if count_wifi(mid, house) >= C:
        ans = mid
        start = mid + 1
    else:
        end = mid - 1

print(ans)
