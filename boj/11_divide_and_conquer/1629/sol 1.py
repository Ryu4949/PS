A, B, C = map(int, input().split())
def mod(a, b, c):
    if b == 1:
        return (a ** b) % c

    else:
        if b % 2:
            return ((mod(a, b // 2, c)**2) * a) % c

        else:
            return (mod(a, b // 2, c)**2) % c

print(mod(A, B, C))