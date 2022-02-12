#시간초과
#for문은 중첩될 때만 오래걸리고 따로 떨어져있으면 크게 영향이 없다는 막연한 생각이었는데
#응 아니고
#(보통) 1초 = 2000만번 생각하고 for문은 가급적 한번에 끝내도록



n, m = map(int, input().split())
no_mix = []
for _ in range(m):
    no_mix.append(list(map(int, input().split())))

ice_cream = list(range(1, n+1))

cnt = 0

ice_set = []
for i in range(1, n-1):
    for j in range(i+1, n):
        for k in range(j+1, n+1):
            ice_set.append([i, j, k])

for i in ice_set:
    for l in no_mix:
        if l[0] in i and l[1] in i:
            break
    else:
        cnt += 1

print(cnt)