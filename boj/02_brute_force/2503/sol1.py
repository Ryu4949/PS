n = int(input())
call = []
for _ in range(n):
    call.append(list(input().split()))

nums_list = []

for i in range(1, 10):
    for j in range(1, 10):
        if j != i:
            for k in range(1, 10):
                if k != i and k != j:
                    nums_list.append(str(i)+str(j)+str(k))

def check_nums(num):
    cnt = 0
    for i in range(n):
        strike = 0
        ball = 0
        for j in range(3):
            if num[j] == call[i][0][j]:
                strike += 1
        for j in range(3):
            if num[j] != call[i][0][j] and num[j] in call[i][0]:
                ball += 1
        if strike == int(call[i][1]) and ball == int(call[i][2]):
            cnt += 1

    if cnt == n:
        return True
    else:
        return False

result = 0
for i in nums_list:
    if check_nums(i):
        result += 1

print(result)