#휴게소간 가능한 거리는 1 ~ L-2
#마찬가지로 gap을 정하고, 그 gap으로 가능하다면 더 높은 gap을 설정해서 다시 검토
#불가능하다면 낮은 gap으로 검토
#검토 방법은 예를 들어 구간 설정을 300으로 했고, 현재 휴게소 없는 구간이 1 ~ 599 라면
#(599 - 1) // 300 만큼 추가가능

def count_rest(gap, array):
    cnt = 0
    for i in range(1, len(array)):
        if (array[i] - array[i-1]) % gap == 0:
            cnt += max((array[i] - array[i-1]) // gap -1, 0)
        else:
            cnt += (array[i] - array[i - 1]) // gap
    return cnt

N, M, L = map(int, input().split())
rest = list(map(int, input().split()))
rest.append(0)
rest.append(L)
rest.sort()

start = 1
end = L- 1

ans = 0
while start <= end:
    mid = (start + end) // 2
    if count_rest(mid, rest) > M:
        start = mid + 1
    else:
        ans = mid
        end = mid - 1

print(ans)
