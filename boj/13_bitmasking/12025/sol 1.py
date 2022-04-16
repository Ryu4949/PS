password = list(input())
K = int(input())

key = []
for i in range(len(password)):
    if password[i] == '1' or password[i] == '6':
        key.append((('1', '6'), i))
    elif password[i] == '2' or password[i] == '7':
        key.append((('2', '7'), i))

if 2**len(key) < K:
    print(-1)
    exit()

for i in range(len(key)):
    if (K-1) & (1<<(len(key)-1-i)):
        password[key[i][1]] = key[i][0][1]
    else:
        password[key[i][1]] = key[i][0][0]

print(''.join(password))
