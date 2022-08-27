N, M = map(int, input().split())

if (N+M)%2 or M > N:
    print(-1)
else:
    print(max((N+M)//2, (N-M)//2), min((N+M)//2, (N-M)//2))