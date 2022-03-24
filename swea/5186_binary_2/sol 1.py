#소수를 이진수로 바꿔주는 함수
def binary(n):
    rlt = ''
    #2를 계속 곱하면서 1이 되거나, 소수부가 원래의 소수와 같아질 때까지
    while True:
        n *= 2
        #1이상이 되면 rlt에 1을 추가하고, 다시 소수부만 남김
        if n >= 1:
            rlt += '1'
            n -= 1
        #2를 곱했을 때 1이 넘어가지 않으면 0추가
        else:
            rlt += '0'

        #길이가 13이상이면 overflow
        if len(rlt) >= 13:
            return 'overflow'

        #만약 2를 곱했을 때 정확히 1이되거나(위에서 1이상이면 1을 빼주니까 n == 0)
        #원래의 소수와 같아지게 되면 rlt 반환
        if n == N or n == 0:
            return rlt


T = int(input())
for tc in range(1, T+1):
    N = float(input())

    print(f'#{tc} {binary(N)}')