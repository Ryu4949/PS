str = input()
check = input()

N = len(str)
K = len(check)

cnt = 0
i = 0
while True:
    if str[i:i+K] == check:
        cnt += 1
        i += K
    else:
        i += 1

    if i >= N:
        break

print(cnt)