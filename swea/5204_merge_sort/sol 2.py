def mergesort(start, end):
    global cnt
    if start == end:
        return nums[start]

    mid = (end-start+1) // 2

    left = mergesort(start, mid)
    right = mergesort(mid+1, end)

    merged_arr = []
    l = h = 0
    while l < len(left) and h < len(right):
        if left[l] < right[h]:
            merged_arr.append(left[l])
            l += 1
        else:
            merged_arr.append(right)
            h += 1

    if left[-1] > right[-1]:
        cnt += 1
    merged_arr += left[l:]
    merged_arr += right[h:]
    return merged_arr

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = [*map(int, input().split())]
    cnt = 0

    print(f'#{tc} {mergesort(0, N-1)[N//2]} {cnt}')
