T= int(input())
for tc in range(1, T+1):
    a = input()
    laser = '()'

    #존재하는 막대기
    #자른 횟수 한번 증가할 때마다 존재하는 막대기 만큼 잘린 갯수 추가
    #닫히는 게 존재하면 잘린 막대기에 닫힌 거 개수만큼 추가하고 존재막대기에 그만큼 빼줌

    exist = 0
    cut = 0

    for i in range(len(a)):
        if a[i] == '(':
            if a[i+1] ==')':
                cut += exist
            else:
                exist += 1
        else:
            if a[i-1] == '(':
                pass
            else:
                exist -= 1
                cut += 1

    print(f'#{tc} {cut}')