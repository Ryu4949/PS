#회문인지 여부를 판단하는 함수
def is_palindrome(word):
    for i in range(len(word)//2):
        if word[i] != word[-i-1]:
            return False
    return True

#배열이 주어졌을 때, 회문 길이의 최대값을 찾는 함수
def len_palindrome(array):
    for l in range(100, 0, -1):
        for i in range(100):
            for j in range(100 - l + 1):
                if is_palindrome(array[i][j:j + l]):
                    return l

for tc in range(1, 11):
    t = int(input())
    board = [list(input()) for _ in range(100)]

    #주어진 글자판에서 가로방향으로 회문 및 최대 길이 확인
    hor_max = len_palindrome(board)

    #세로를 확인하기 위하여 전치
    for i in range(100):
        for j in range(100):
            if i > j:
                board[i][j], board[j][i] = board[j][i], board[i][j]

    #세로방향의 회문 및 최대 길이 확인
    ver_max = len_palindrome(board)

    #둘 중에 큰 것으로 출력
    if hor_max >= ver_max:
        max_len = hor_max
    else:
        max_len = ver_max

    print(f'#{tc} {max_len}')