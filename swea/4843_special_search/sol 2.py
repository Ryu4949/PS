t = int(input())
for num in range(1, t+1):
    n = int(input())
    nums = list(map(int, input().split()))
    #내림차순 정렬
    for i in range(n-1, 0, -1):
        for j in range(i):
            if nums[j] < nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

    print(f'#{num}', end=" ")
    #짝수 인덱스일 때는 큰수부터, 홀수 인덱스일때는 작은수부터(즉 리스트의 끝부터) 출력
    for i in range(10):
        if i % 2 == 0:
            print(nums[i//2], end=" ")
        else:
            print(nums[-(i+1)//2], end=" ")
    print()