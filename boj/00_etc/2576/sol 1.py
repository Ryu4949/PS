s = 0
m = 100
for _ in range(7):
    num = int(input())
    if num%2:
        s += num
        m = min(m, num)

if not s:
    print(-1)
else:
    print(s)
    print(m)