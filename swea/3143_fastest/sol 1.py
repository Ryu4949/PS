# 문자열과 단축문자열이 주어질 때 키를 눌러야할 횟수를 구하는 함수
def shorten(word, shortcut):
    # cnt는 단축키를 누르는 횟수, i는 원래 문자열을 따라갈 인덱스
    cnt = 0
    i = 0
    while i < len(word):

        # 주어진 문자열의 i번째 글자가 단축문자열의 첫번째 글자와 같으면 확인
        if word[i] == shortcut[0]:

            # 일치하면 cnt늘려주고, 다음 i는 단축문자열의 길이만큼 건너뜀
            if word[i:i + len(shortcut)] == shortcut:
                cnt += 1
                i += len(shortcut)

            # 첫글자는 같은데 일치하지 않으면 i에만 1 증가
            else:
                i += 1
        else:
            i += 1

    # 단축문자열을 한번 누를때마다 단축문자열의 길이에서 1을 뺀만큼 키를 누를 횟수가 줄어듦
    return len(word) - cnt * (len(shortcut) - 1)


T = int(input())
for tc in range(1, T + 1):
    A, B = input().split()
    print(f'#{tc} {shorten(A, B)}')