T = int(input())
for tc in range(1, T+1):
    words = []
    length = [0] * 5

    for i in range(5):
        words.append(list(input()))
        length[i] = len(words[i])

    max_length = 0
    for i in length:
        if i > max_length:
            max_length = i

    for i in range(5):
        if length [i] < max_length:
            for _ in range(max_length-length[i]):
                words[i].append('')

    print(f'#{tc}', end=" ")
    for i in range(max_length):
        for j in range(5):
            print(words[j][i], end="")
    print()