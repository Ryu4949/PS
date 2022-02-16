def binary_cnt(target, l, r):
    cnt = 0
    while l <= r:
        c = int((l+r)/2)
        if c == target:
            print(f'cnt: {cnt}, l: {l}, r: {r}, c:{c}')
            cnt += 1
            print(f'최종cnt: {cnt}')
            print('----------------------------------------')
            return cnt
        elif c > target:
            r = c - 1
            print(f'cnt: {cnt}, l: {l}, r: {r}, c:{c}')
            cnt += 1
        else:
            l = c + 1
            print(f'cnt: {cnt}, l: {l}, r: {r}, c:{c}')
            cnt += 1

t = int(input())
for num in range(1, t+1):
    P, A, B = map(int, input().split())

    if binary_cnt(A, 1, P) < binary_cnt(B, 1, P):
        print(f'#{num} A')
    elif binary_cnt(A, 1, P) > binary_cnt(B, 1, P):
        print(f'#{num} B')
    else:
        print(f'#{num} 0')

