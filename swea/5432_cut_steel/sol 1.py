T= int(input())
for tc in range(1, T+1):
    a = input()
    laser = '()'

    #자른 횟수 한번 증가할 때마다 존재하는 막대기 만큼 잘린 갯수 추가
    #닫히는 게 존재하면 잘린 막대기에 닫힌 거 개수만큼 추가하고 존재막대기에 그만큼 빼줌

    #exist: 현재 존재하는 막대기의 수, cut: 전체 잘린 조각의 개수
    exist = 0
    cut = 0

    for i in range(len(a)):
        #레이저가 있으면 그 시점의 exist만큼 잘린 조각이 생성되므로 cut에 exist를 더해줌
        if a[i] == '(':
            if a[i+1] ==')':
                cut += exist
            #'('가 연속되면 새로운 막대기가 추가 되므로 exist에 1을 더해줌
            else:
                exist += 1
        else:
            #'()'인 경우는 위에 포함되므로 pass
            if a[i-1] == '(':
                pass
            #')'가 연속되는 경우는 막대기의 끝을 나타내므로 exist 1 감소하고 cut은 1 증가
            else:
                exist -= 1
                cut += 1

    print(f'#{tc} {cut}')