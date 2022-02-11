a, b = map(int, input().split())
i = 0
while a != b:
    if b < a:
        break
    elif b % 2 == 1 and str(b)[-1] != '1':
        break

    if b % 2 == 0:
        b //= 2
    elif str(b)[-1] == '1':
        b = int(str(b)[:-1])

    i += 1

if a == b:
    print(i+1)
else:
    print(-1)
