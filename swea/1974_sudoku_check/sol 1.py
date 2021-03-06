t = int(input())
for num in range(1, t + 1):
    sudoku = []
    for _ in range(9):
        sudoku.append(list(map(int, input().split())))


    # 스도쿠 확인용 함수
    def check_sudoku(sudoku):
        trans_sudoku = list(zip(*sudoku))
        # 가로검증
        for i in sudoku:
            if len(i) != len(set(i)):
                return 0
        # 세로검증
        for i in trans_sudoku:
            if len(i) != len(set(i)):
                return 0
        # 3*3검증
        for i in range(3):
            for j in range(3):
                three_by_three = sudoku[3 * i][3 * j:3 * j + 3] + sudoku[3 * i + 1][3 * j:3 * j + 3] + sudoku[
                                                                                                           3 * i + 2][
                                                                                                       3 * j:3 * j + 3]
                if len(set(three_by_three)) != 9:
                    return 0
        return 1


    print(f'#{num}', end=" ")
    print(check_sudoku(sudoku))