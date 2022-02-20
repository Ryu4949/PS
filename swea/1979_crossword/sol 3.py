t = int(input())
for num in range(1, t+1):
    n, k = map(int, input().split())
    data = []
    for _ in range(n):
        data.append(list(input().split()))
    #세로 점검용 전치
    trans_data = list(zip(*data))

    cnt = 0
    #각 행을 하나의 문자열로 합쳐주고 '0'을 기준으로 구분
    #그리고 '1'로 이루어진 k길이의 문자열이 있는지 확인
    for i in data:
        for j in list(''.join(i).split('0')):
            if j == '1'*k:
                cnt += 1

    for i in trans_data:
        for j in list(''.join(i).split('0')):
            if j == '1' * k:
                cnt += 1

    print(f'#{num} {cnt}')