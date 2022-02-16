#탐색의 횟수를 세는 함수 설정
def binary_cnt(target, l, r):
    cnt = 0
    while l <= r:
        c = int((l+r)/2)
        if c == target:
            cnt += 1
            return cnt
        elif c > target:
            r = c
            cnt += 1
        else:
            l = c
            cnt += 1

t = int(input())
for num in range(1, t+1):
    P, A, B = map(int, input().split())

    #카운트가 적은 쪽이 승리
    if binary_cnt(A, 1, P) < binary_cnt(B, 1, P):
        print(f'#{num} A')
    elif binary_cnt(A, 1, P) > binary_cnt(B, 1, P):
        print(f'#{num} B')
    else:
        print(f'#{num} 0')

