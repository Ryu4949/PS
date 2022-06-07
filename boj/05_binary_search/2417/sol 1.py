N = int(input())

start = 0
end = 2**63

answer = 0
while start <= end:
    mid = (start+end)//2
    if mid**2 >= N:
        end = mid - 1
        answer = mid
    else:
        start = mid + 1

print(answer)