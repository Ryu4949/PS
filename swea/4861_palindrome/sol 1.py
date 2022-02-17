# 회문 판별 함수
def is_palindrome(word):
    for i in range(len(word) // 2):
        if word[i] != word[-i - 1]:
            return False
    return True


# 회문을 발견하면 출력하는 함수
def print_palindrome(array):
    # 가로 먼저 확인하고, 회문은 1개 존재한다고 했으므로, 발견하면 바로 return
    for i in range(N):
        for j in range(N - M + 1):
            if is_palindrome(array[i][j:j + M]):
                return ''.join(array[i][j:j + M])

    # 가로에서 발견되지 않았으면 세로 점검을 위해 전치
    for i in range(N):
        for j in range(N):
            if i > j:
                array[i][j], array[j][i] = array[j][i], array[i][j]

    # 회문이 발견되면 return
    for i in range(N):
        for j in range(N - M + 1):
            if is_palindrome(array[i][j:j + M]):
                return ''.join(array[i][j:j + M])


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    board = [list(input()) for _ in range(N)]

    print(f'#{tc} {print_palindrome(board)}')