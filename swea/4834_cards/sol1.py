t = int(input())
for num in range(1, t+1):
    n = int(input())
    card = input()
    
    #카드의 개수 저장
    cnt = [0] * 10

    #card 정보 입력을 문자열로 받아서 앞에서부터 하나씩 순회
    #해당 숫자의 위치에 카운트 +1
    for i in card:
        cnt[int(i)] += 1

    #max_cnt에 최대 개수 저장, 그리고 최대 개수를 갖는 인덱스(=최대개수의 카드번호)를 max_idx에 저장
    max_idx = 0
    max_cnt = 0
    
    #0부터 차례대로 비교해주면서 최대값과 그 위치를 저장
    #새로 비교하는 개수가 기존의 개수 이상이면 교체
    #작은 수부터 비교하기 때문에 장수가 같은 경우에 자동으로 큰 쪽을 출력함
    for i in range(10):
        if cnt[i] >= max_cnt:
            max_cnt = cnt[i]
            max_idx = i

    print(f'#{num} {max_idx} {max_cnt}')