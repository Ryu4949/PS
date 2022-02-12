N,M,K=map(int,input().split())

cnt=0
while cnt!=K:
    if N>2*M:
        N -= 1
    else:
        M -= 1
    cnt += 1

print(min(N//2,M))