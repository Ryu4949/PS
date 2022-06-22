import sys
input = sys.stdin.readline

N = int(input())
nums = [*map(int, input().split())]
nums.sort()

cnt = 0

print(nums)
if N <= 2:
    print(0)
else:
    for i in range(N-2):
        for j in range(i+1, N-1):
            start1 = j+1
            end1 = N-1
            start2 = j+1
            end2 = N-1
            while start1 <= end1:
                mid = (start1+end1)//2
                if nums[start1]+nums[end1]+nums[mid] >= 0:
                    end1 = mid-1
                else:
                    start1 = mid+1

            while start2 <= end2:
                mid = (start2+end2)//2
                if nums[start2]+nums[end2]+nums[mid] > 0:
                    end2 = mid-1
                else:
                    start2 = mid+1

            print(f'i, j: {i, j}, start1: {start1}, start2: {start2}')
            cnt += (start2-start1+1)

print(cnt)