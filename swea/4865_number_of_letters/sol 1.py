T = int(input())
for tc in range(1, T + 1):
    # str1에 겹치는 글자가 있을 수 있으므로 set을 사용
    str1 = set(input())
    str2 = input()

    # 가장 개수가 많은 글자의 개수를 저장할 변수
    max_cnt = 0

    # str1에서 한글자씩 기준으로 str2에서 확인하면서 최대 개수를 도출
    for i in str1:
        cnt = 0
        for j in str2:
            if i == j:
                cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt

    print(f'#{tc} {max_cnt}')