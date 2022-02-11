n = int(input())
prob = input()

cnt = 0
for i in range(1, n):
    if prob[i] != prob[i-1]:
        cnt += 1

if cnt % 2 == 0:
    print(cnt//2 + 1)
else:
    print(cnt//2 + 2)