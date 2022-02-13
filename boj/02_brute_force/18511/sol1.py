N, K = map(int, input().split())

k = list(input().split())
k.sort(reverse=True)

idx = -1
for i in range(len(str(N))):
    if str(N)[i] not in k:
        idx = i
        break

point = None
for i in k:
    if i <= str(N)[idx]:
        point = i
        break
else:
    point = ''

if idx >= 0:
    print(int(str(N)[:idx] + point + max(k) * (len(str(N))-idx-1)))
else:
    print(N


'''
주의해야할 반례
510 3
157
'''