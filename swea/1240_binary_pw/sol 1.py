#올바른 암호코드인지 확인
def verify(pw):
    ver = 0
    for i in range(8):
        if i != 8 and i % 2 == 0:
            ver += int(pw[i]) * 3
        else:
            ver += int(pw[i])

    if ver % 10 == 0:
        return True
    else:
        return False

#배열이 주어지면 그 중에서 암호코드를 찾는 함수
def find_key(lst):
    #각 줄마다 확인하는데 1이 하나도 없다면 다음줄로
    for i in range(N):
        if '1' not in lst[i]:
            continue
        #7자리씩 끊어서 8번 모두 수와 대응된다면 그만큼을 반환
        for j in range(M):
            for k in range(8):
                #확인하다가 수에 대응되지 않는 7자리 이진코드를 만난다면 중단
                if lst[i][j+7*k:j+7*k+7] not in key:
                    break
            else:
                return lst[i][j:j+56]

P = {
        '0001101': 0,
        '0011001': 1,
        '0010011': 2,
        '0111101': 3,
        '0100011': 4,
        '0110001': 5,
        '0101111': 6,
        '0111011': 7,
        '0110111': 8,
        '0001011': 9,
}

key = P.keys()

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    pw_list = [input() for _ in range(N)]
    pw = find_key(pw_list)

    #56자리 코드를 앞에서 7자리씩 끊어서 대응되는 수를 code에 추가
    code = []
    for i in range(8):
        code.append(P[pw[7*i:7*i+7]])

    ans = 0
    #유효한 코드라면 대응되는 수를 ans에 더해줌
    if verify(code):
        for i in code:
            ans += int(i)

    print(f'#{tc} {ans}')
