
N, M = map(int,input().split())
icecream = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    icecream[a].append(b)
    icecream[b].append(a)

cnt = 0

for i in range(1,N-1):
    for j in range(i+1,N):
        for k in range(j+1,N+1):
            if j not in icecream[i] and k not in icecream[i] and k not in icecream[j]:
                cnt += 1

print(cnt)