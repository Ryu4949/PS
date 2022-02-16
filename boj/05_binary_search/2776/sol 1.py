T = int(input())
for _ in range(T):
    N = int(input())
    note1 = list(map(int, input().split()))
    M = int(input())
    note2 = list(map(int, input().split()))
    note1.sort()

    def binary_search(target, array, start, end):
        while start <= end:
            mid = (start + end) // 2
            if array[mid] == target:
                return 1
            elif array[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return 0

    for i in note2:
        print(binary_search(i, note1, 0, N-1))