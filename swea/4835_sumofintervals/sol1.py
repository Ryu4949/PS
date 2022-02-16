t = int(input())
for num in range(1, t+1):
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))

    #최대구간합, 최소구간합을 저장할 변수. 초기값 설정
    max_sub = 0
    min_sub = (m+1) * 10000

    #입력받은 리스트의 처음부터 길이 m인 부분 리스트로 비교
    for i in range(n-m+1):
        #해당 구간의 구간합 저장
        subtotal = 0
        for j in nums[i:i+m]:
            subtotal += j
            
        #구간합이 기존의 최대 구간합보다 크다면 새로 저장
        if subtotal > max_sub:
            max_sub = subtotal
        #구간합이 기존의 최소 구간합보다 작다면 새로 저장
        if subtotal < min_sub:
            min_sub = subtotal

    print(f'#{num} {max_sub-min_sub}')