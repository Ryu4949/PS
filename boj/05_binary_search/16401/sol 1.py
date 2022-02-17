#한 명당 최소 length를 주려고 할 때 나올 수 있는 과자의 개수
def count_cookie(array, length):
    cnt = 0
    for i in array:
        cnt += i // length
    return cnt

M, N = map(int, input().split())
cookies = list(map(int, input().split()))

start = 1
end = max(cookies)

ans = 0
while start <= end:
    mid = (start + end) // 2
    if count_cookie(cookies, mid) >= M:
        ans = mid
        start = mid + 1
    else:
        end = mid - 1

print(ans)