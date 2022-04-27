N = int(input())
pos = []
neg = []
one = []
for _ in range(N):
    a = int(input())
    if a > 1:
        pos.append(a)
    elif a == 1:
        one.append(a)
    else:
        neg.append(a)

pos.sort(reverse=True)
neg.sort()

ans = 0
for i in range(len(pos)//2):
    a, b = pos[2*i], pos[2*i+1]
    ans += a * b

if len(pos)%2:
    ans += pos[-1]

for i in range(len(neg)//2):
    a, b = neg[2*i], neg[2*i+1]
    ans += a * b

if len(neg)%2:
    ans += neg[-1]

ans += 1*len(one)

print(ans)

