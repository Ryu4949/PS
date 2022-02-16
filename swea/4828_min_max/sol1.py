t = int(input())
for num in range(1, t+1):
    n = int(input())
    nums = list(map(int, input().split()))

    #min에 최소값, max에 최대값 저장. 처음에는 입력받은 리스트의 처음 값을 저장
    min = nums[0]
    max = nums[0]

    #그 다음 값부터 순회하면서 기존 min보다 작으면 min 교체, 기존 max보다 크면 max 교체
    for i in nums[1:]:
        if i < min:
            min = i
        if i > max:
            max = i

    print(f'#{num} {max-min}')