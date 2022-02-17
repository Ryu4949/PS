t = int(input())
for num in range(1, t+1):
    n = int(input())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))

    a_90 = list(zip(*a[::-1]))
    a_180 = list(zip(*a_90[::-1]))
    a_270 = list(zip(*a_180[::-1]))

    print(f'#{num}')
    for i in range(n):
        print(''.join(map(str, a_90[i])), end=" ")
        print(''.join(map(str, a_180[i])), end=" ")
        print(''.join(map(str, a_270[i])))