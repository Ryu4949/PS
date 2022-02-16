N = int(input())
num_list = list(map(int, input().split()))
M = int(input())
check = list(map(int, input().split()))

num_list.sort()

def binary(data, target, start, end):
    while start <= end:
        mid = (start + end)//2
        if data[mid] == target:
            return mid
        elif data[mid] > target:
            return binary(data, target, start, mid-1)
        else:
            return binary(data, target, mid+1, end)

for i in check:
    if binary(num_list, i, 0, len(num_list)-1) == None:
        print(0)
    else:
        print(1)

