number = '1231234'
N = len(number)
rlt = ''

k = 3
idx = 0
while k > 0:
    sub_max = '0'
    for i in range(idx, min(N, idx+k+1)):
        if number[i] > sub_max:
            sub_max = number[i]
            idx = i
            cnt = i-idx
            print(f'sub_max: {sub_max}, cnt: {cnt}')
    rlt += sub_max
    idx += 1
    k -= idx


