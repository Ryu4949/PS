#가위바위보
def game(i, j): #i < j
    if data[i-1] == data[j-1]:  #비긴 경우 더 작은 번호가 승리
        return i
    elif data[i-1] == 1:    #i가 가위일 때
        if data[j-1] == 2:
            return j
        else:
            return i
    elif data[i-1] == 2:    #i가 바위일 때
        if data[j-1] == 1:
            return i
        else:
            return j
    else:   #i가 보일 때
        if data[j-1] == 1:
            return j
        else:
            return i

#토너먼트 승자 찾기
def tournament(i, j):
    if i == j:  #1명이면 바로 반환
        return i
    else:   #2명 이상이면 그룹나눠서 다시
        left = tournament(i, (i+j)//2)  #왼쪽그룹의 승자 찾기
        right = tournament((i+j)//2+1, j)   #오른쪽 그룹의 승자 찾기
        return game(left, right)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))

    print(f'#{tc} {tournament(1, N)}')