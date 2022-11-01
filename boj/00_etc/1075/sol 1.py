N = int(input())
F = int(input())

N //= 100
N *= 100

while True:
    if not N%F:
        break
    else:
        N += 1

print(str(N)[-2:])