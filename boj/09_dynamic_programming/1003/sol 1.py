#시간초과
#아니 이거 확인하라는 문제 아니었음?

T = int(input())
for _ in range(T):
    N = int(input())

    d = [0] * 41
    cnt_zero = 0
    cnt_one = 0

    def fibo(x):
        global cnt_zero, cnt_one
        if x == 0:
            cnt_zero += 1

        if x == 1:
            cnt_one += 1

        if x <= 1:
            return x

        return fibo(x - 1) + fibo(x - 2)

    fibo(N)

    print(cnt_zero, cnt_one)