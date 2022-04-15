password = list(input())
K = int(input())
print(password)
key = []
for i in range(len(password)):
    if password[i] == '1' or password[i] == '6':
        key.append((('1', '6'), i))
    elif password[i] == '2' or password[i] == '7':
        key.append((('2', '7'), i))

for i in range(len(key)):
    if (K-1) & (1<<i):
        password[key[i][1]] = 