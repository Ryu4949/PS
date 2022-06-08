import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    nums = [*map(int, input().split())]
    nums.sort()

    min_gap = 10**9
    cnt = 1

    for i in range(N-1):
        base = nums[i]
        start = i+1
        end = N-1
        while start <= end:
            mid = (start+end)//2
            if abs(nums[mid]+base-K) < min_gap:
                min_gap = abs(nums[mid]+base-K)
                cnt = 1
                if nums[mid]+base > K:
                    end = mid-1
                elif nums[mid]+base == K:
                    break
                else:
                    start = mid+1
            elif abs(nums[mid]+base-K) > min_gap:
                if nums[mid]+base > K:
                    end = mid-1
                else:
                    start = mid+1
            else:
                cnt += 1
                if nums[mid]+base > K:
                    end = mid-1
                elif nums[mid]+base == K:
                    break
                else:
                    start = mid+1

    print(cnt)