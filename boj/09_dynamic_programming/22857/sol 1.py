N = int(input())
P = list(map(int, input().split()))
d = [0] + [i for i in P]

for i in range(2, N+1):
    for j in range(i):
        d[i] = max(d[i], d[j]+d[i-j])

print(d[-1])