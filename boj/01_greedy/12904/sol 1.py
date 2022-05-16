S = input()
T = input()
while True:
    if T[-1] == 'A':
        T = T[:-1]
    else:
        T = T[::-1]

    print(T)
    if not T:
        print(0)
        break
    elif T == S:
        print(1)
        break
