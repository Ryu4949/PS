import sys
input = sys.stdin.readline

N = int(input())
liquids = [*map(int, input().split())]

liquids.sort()

min_sum = 10**10
liquid1 = 0
liquid2 = 0

for i in range(N-1):
    start = i+1
    end = N-1
    while start <= end:
        mid = (start+end)//2
        liquid_sum = liquids[i]+liquids[mid]
        if abs(liquid_sum) < min_sum:
            min_sum = abs(liquid_sum)
            liquid1 = liquids[i]
            liquid2 = liquids[mid]
            if liquid_sum < 0:
                start = mid + 1
            elif liquid_sum == 0:
                print(liquid1, liquid2)
                exit()
            else:
                end = mid - 1
        else:
            if liquid_sum < 0:
                start = mid + 1
            else:
                end = mid - 1

print(liquid1, liquid2)

