#휴게소간 가능한 거리는 1 ~ L-2
#마찬가지로 gap을 정하고, 그 gap으로 가능하다면 더 높은 gap을 설정해서 다시 검토
#불가능하다면 낮은 gap으로 검토
#검토 방법은 예를 들어 구간 설정을 300으로 했고, 현재 휴게소 없는 구간이 1 ~ 599 라면
#(599 - 1) // 300 만큼 추가가능

def count_rest(gap, array):
    cnt = 0
    max_gap = 0
    for i in range(1, len(array)):
        cnt += max((array[i] - array[i-1]) // gap -1, 0)
    return cnt

N, M, L = map(int, input().split())
rest = list(map(int, input().split()))
rest.append(0)
rest.append(L)
rest.sort()
print(f'현재 휴게소: {rest}')

start = 1
end = L- 1

ans = 0
while start <= end:
    mid = (start + end) // 2
    print(f'현재 ans: {ans}')
    print(f'mid: {mid}, count_rest: {count_rest(mid, rest)}')
    if count_rest(mid, rest) == M:
        ans = mid
        end = mid - 1
    elif count_rest(mid, rest) > M:
        start = mid + 1
    else:
        end = mid - 1
print(ans)


#0, 1, 3, 1, 1,


#0 82 201 411 555 622 755 800
# 82 60 59 53 52 53 52 72 72 67 67 66 45


#100 120 140 160 180