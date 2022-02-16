N = int(input())
nums = list(map(int, input().split()))
M = int(input())
cards = list(map(int, input().split()))

nums.sort()

def card(target, array, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return 1
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0

for i in cards:
    print(card(i, nums, 0, N-1))
