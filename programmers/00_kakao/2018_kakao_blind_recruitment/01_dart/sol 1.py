def solution(dartResult):
    answer = 0
    score = [[0, 0]]
    i = 0
    j = 1
    while True:
        if not dartResult[j-1].isdigit() and dartResult[j].isdigit():
            score.append([0, dartResult[i:j]])
            i = j
            j += 1
        elif j == len(dartResult)-1:
            score.append([0, dartResult[i:j+1]])
            break
        else:
            j += 1

    def calculate(str, idx):
        nonlocal score

        point = 0
        for i in range(len(str)):
            if i < len(str)-1 and not str[i + 1].isdigit() and str[i].isdigit():
                point += int(str[i])
            elif i < len(str)-1 and str[i + 1].isdigit() and str[i].isdigit():
                point += int(str[i] + str[i + 1])
            elif str[i].isupper():
                if str[i] == 'D':
                    point **= 2
                elif str[i] == 'T':
                    point **= 3
            elif str[i] == '*':
                score[idx - 1][0] *= 2
                point *= 2
            elif str[i] == '#':
                point *= (-1)
        return point

    for i in range(1, 4):
        score[i][0] = calculate(score[i][1], i)

    for i in range(1, 4):
        answer += score[i][0]
    return answer




print(solution("1D2S#10S"))