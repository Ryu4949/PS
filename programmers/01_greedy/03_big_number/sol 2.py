num = '1231234'

N = len(num)
rlt = ''
k = 3
for i in range(N):
    if k > 0:
        for j in range(i+1, min(N, i+1+k)):
            if num[i] < num[j]:
                k -= 1
                break
        else:
            rlt += num[i]
    else:
        rlt += num[i]

print(rlt)