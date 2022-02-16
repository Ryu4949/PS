t = int(input())
for num in range(1, t+1):
    a = list(range(1, 13))
    n, k = map(int, input().split())

    ans = 0
    #전체 부분집합을 돌면서 원소의 수와 부분집합의 합을 저장
    for i in range(1<<12):
        rlt = 0
        cnt = 0
        for j in range(12):
            if i & (1 << j):
                rlt += a[j]
                cnt += 1
        #부분집합의 원소의 수와 부분집합의 합이 입력된 값에 일치할 때만 ans에 1을 더해줌
        if rlt == k and cnt == n:
            ans += 1

    print(f'#{num} {ans}')