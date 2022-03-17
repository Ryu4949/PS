def find_cube(num):
    i = 0
    while True:
        if i**3 == num:
            return i
        elif i**3 > num:
            return -1
        i += 1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc} {find_cube(N)}')