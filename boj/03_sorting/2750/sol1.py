n = int(input())
data = []
for i in range(n):
    data.append(int(input()))

#1. 버블정렬
for i in range(n-1, 0, -1):
    for j in range(i):
        if data[j] > data[j+1]:
            data[j], data[j+1] = data[j+1], data[j]

for i in data:
    print(i)

#2. 카운팅 정렬
max_num = max(data)
cnt = [0] * (max_num+1)

for i in data:
    cnt[i] += 1

for i in range(1, len(cnt)):
    cnt[i] += cnt[i-1]

tmp = [0] * n

for i in range(n-1, -1, -1):
    cnt[data[i]] -= 1
    tmp[cnt[data[i]]] = data[i]

for i in tmp:
    print(i)