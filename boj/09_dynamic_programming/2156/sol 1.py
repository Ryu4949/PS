'''
처음엔 계단문제랑 비슷한줄 알았는데 아니네?
맞네 d[i]를 i번쨰 잔을 마실 경우에 최대가 되는 값으로 놓고 d[N]까지 구해준 다음에 d 리스트의 최대값을 가져오면 된다고 생각했으나..
아니네
'''

N = int(input())
wine = [0]
for _ in range(N):
    wine.append(int(input()))

d = [0] * (N+1)

def max_wine(N):
    if N == 1:
        return wine[1]
    elif N == 2:
        return wine[1] + wine[2]
    elif N == 3:
        return max(wine[1]+wine[3], wine[2]+wine[3], wine[1]+wine[2])
    else:
        d[1] = wine[1]
        d[2] = wine[2]+wine[1]
        d[3] = max(wine[1]+wine[3], wine[2]+wine[3])

        for i in range(4, N+1):
            d[i] = max(d[i-3]+wine[i]+wine[i-1], d[i-2]+wine[i], d[i-4]+wine[i]+wine[i-1])
        return max(d)

print(max_wine(N))
