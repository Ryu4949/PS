N = int(input())
A = []
B = []
C = []
D = []

for _ in range(N):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

sum_AB = []
sum_CD = []

for i in range(N):
    for j in range(N):
        sum_AB.append(A[i]+B[j])
        sum_CD.append(C[i]+D[j])

sum_AB.sort()
sum_CD.sort()

l = 0
r = len(sum_CD)-1
cnt = 0

while True:
    tmp = sum_AB[l] + sum_CD[r]
    if tmp > 0:
        r -= 1
    elif tmp < 0:
        l += 1
    else:
        sl = 1
        sr = 1
        ll = l+1
        rr = r-1
        while ll < len(sum_AB) and sum_AB[l] == sum_AB[ll]:
            sl += 1
            ll += 1

        while rr >= 0 and sum_CD[r] == sum_CD[rr]:
            sr += 1
            rr -= 1

        cnt += sl*sr
        l = ll
        r = rr

    if l >= len(sum_AB) or r < 0:
        break

print(cnt)