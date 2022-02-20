T = int(input())
for tc in range(1, T+1):
    words = []
    length = [0] * 5

    #문자열을 입력받으면서 그 문자열의 길이를 저장할 리스트를 별도로 생성
    for i in range(5):
        words.append(list(input()))
        length[i] = len(words[i])

    #가장 긴 문자열의 길이 확인
    max_length = 0
    for i in length:
        if i > max_length:
            max_length = i

    #가장 긴 문자열보다 짧은 문자열에 대해서는 부족한 길이만큼 빈문자열 추가
    for i in range(5):
        if length [i] < max_length:
            for _ in range(max_length-length[i]):
                words[i].append('')

    #출력
    print(f'#{tc}', end=" ")
    for i in range(max_length):
        for j in range(5):
            print(words[j][i], end="")
    print()