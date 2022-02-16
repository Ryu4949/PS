t = int(input())
for num in range(1, t+1):
    n = int(input())
    nums = list(map(int, input().split()))
    for i in range(n):
        if i % 2 == 0:
            for j in range(n-1, i, -1):
                if nums[j] > nums[j-1]:
                    nums[j], nums[j-1] = nums[j-1], nums[j]

        else:
            for j in range(n-1, i, -1):
                if nums[j] < nums[j-1]:
                    nums[j], nums[j-1] = nums[j], nums[j-1]

    print(f'#{num}', end=" ")
    for i in nums:
        print(i, end=" ")
    print()