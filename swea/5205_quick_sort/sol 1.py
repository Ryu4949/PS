def quick_sort(arr, start, end):
    if start >= end:    #원소가 1개인 경우 바로 return
        return
    pivot = start   #pivot은 맨 처음 원소, left는 pivot바로 다음, right는 가장 오른쪽 원소
    left = start + 1
    right = end

    while left <= right:    #left, right가 교차하지 않는동안 반복
        while left <= end and arr[left] <= arr[pivot]:  #left는 pivot보다 큰값 만날 때까지 오른쪽으로 이동
            left += 1
        while right > start and arr[right] >= arr[pivot]:   #right는 pivot보다 작은값 만날때까지 왼쪽으로 이동
            right -= 1

        if left > right:    #만약 left와 right가 엇갈렸다면 작은값인 right의 값을 pivot의 값과 바꿈
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:   #엇갈리지 않았다면 left값과 right값 교환
            arr[left], arr[right] = arr[right], arr[left]

    quick_sort(arr, start, right-1) #pivot을 중심으로 분할한 후 왼쪽과 오른쪽에 대해 다시 정렬
    quick_sort(arr, right+1, end)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    quick_sort(nums, 0, N-1)

    print(f'#{tc} {nums[N//2]}')