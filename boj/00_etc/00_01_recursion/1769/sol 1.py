num = '1234567'

def three(i, n: str):
    if len(n) == 1:
        print(i)
        print("YES") if int(n) % 3 == 0 else print("NO")
        return

    a = 0
    for j in n:
        a += int(j)

    return three(i+1, str(a))

ans = three(0, num)