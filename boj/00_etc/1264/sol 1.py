while True:
    sentence = input()
    if sentence == '#':
        break
    cnt = 0
    for chr in sentence:
        if chr in 'aeiouAEIOU':
            cnt += 1
    print(cnt)