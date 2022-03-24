#주어진 수 n을 이진수로 변환하는 함수
def binary(n):
    bi = ['0'] * 4

    i = 3
    while n > 0:
        bi[i] = str(n % 2)
        n //= 2
        i -= 1

    return ''.join(bi)

hex = {
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15
}

T = int(input())
for tc in range(1, T+1):
    N, H = input().split()
    rlt = ''
    #주어진 16진수에서
    for i in H:
        #0~9
        if i.isdigit():
            rlt += binary(int(i))
        #A~F
        else:
            rlt += binary(hex[i])

    print(f'#{tc} {rlt}')