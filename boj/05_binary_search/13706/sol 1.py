N = int(input())
start = 1
end = N
while start <= end:
    mid = (start + end) // 2
    if mid**2 >= N:
        end = mid - 1
    else:
        start = mid + 1

print(start)