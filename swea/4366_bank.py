def binary(nums):
    rlt = 0
    for i in range(len(nums)):
        if nums[len(nums)-i-1]:
            rlt += 2 ** i

    return rlt

def trinary(nums):
    rlt = 0
    for i in range(len(nums)):
        if nums[len(nums) - i - 1]:
            rlt += (3 ** i) * nums[len(nums)-i-1]

    return rlt

T = int(input())
for tc in range(1, T+1):
    bin = list(map(int, list(input())))
    tri = list(map(int, list(input())))

    bi = []
    tr = []

    for i in range(len(bin)):
        for j in range(2):
            bin[i] = (bin[i] + 1) % 2
            bi.append(binary(bin))

    for i in range(len(tri)):
        for j in range(3):
            tri[i] = (tri[i] + 1) % 3
            tr.append(trinary(tri))

    for i in bi:
        if i in tr:
            print(f'#{tc} {i}')
            break