N = int(input())
d = [0] * (N+1)

#2보다 큰 N일 때 앞의 두자리는 무조건 10이어야 하고, 101~일 때의 가지수는 d[N-2], 1001~일 때는 d[N-3] ... 임을 이용

def pinary():
    if N == 1:
        return 1
    elif N == 2:
        return 1
    else:
        d[1] = 1
        d[2] = 1

        for i in range(3, N+1):
            for j in range(i-1):
                d[i] += d[j]
            d[i] += 1

        return d[N]

print(pinary())