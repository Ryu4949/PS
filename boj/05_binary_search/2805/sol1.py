N, M = map(int, input().split())
wood = list(map(int, input().split()))
wood.sort()

def cut(h):
    rlt = 0
    for i in wood:
        rlt += i-h if i-h>=0 else 0
    return rlt

def binary(target, start, end):
    while start <= end:
        mid = (start + end)//2
        if cut(mid) == target:
            return mid
        elif cut(mid) >= target:
            start = mid+1
        else:
            end = mid - 1
    return mid

print(binary(M, wood[0], wood[-1]))
