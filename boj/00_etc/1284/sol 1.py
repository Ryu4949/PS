while True:
    num = input()
    if num == '0':
        break
    total = 0
    for n in num:
        if n == '1':
            total += 2
        elif n == '0':
            total += 4
        else:
            total += 3
    total += 1+len(num)
    print(total) 