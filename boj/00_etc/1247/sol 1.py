for tc in range(3):
    N = int(input())
    sign = 0
    for _ in range(N):
        sign += int(input())

    if sign > 0:
        print("+")
    elif sign < 0:
        print("-")
    else:
        print(sign)