#time: 최소 시간을 설정해줌
#최소 시간을 설정해서 -> 그 시간에 모든 친구들이 심사를 받는 게 가능하다면 -> 저장하고 시간을 더 낮게 잡고 다시 탐색
#만약 해당 시간 내에 심사를 마치는 것이 불가능하다면 -> 시간을 늘려서 탐색

#설정한 최소 시간 내에 심사할 수 있는 최대 인원
def check(array, time):
    cnt = 0
    for i in array:
        cnt += time // i
    return cnt

N, M = map(int, input().split())
img = [int(input()) for _ in range(N)]
img.sort()

start = -1
end = max(img) * M + 1

ans = 0
while start <= end:
    mid = (start + end) // 2
    if check(img, mid) >= M:
        ans = mid
        end = mid - 1
    else:
        start = mid + 1

print(ans)
