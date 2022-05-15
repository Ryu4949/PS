import sys
input = sys.stdin.readline

def is_prime(n):
    cnt = 0
    for i in range(2, int(n**(1/2))+1):
        if not n%i:
            cnt += 1
    if cnt == 0:
        return True
    else:
        return False

T = int(input())
for _ in range(T):
    N = int(input())
    a = N//2
    b = N-a
    while True:
        if is_prime(a) and is_prime(b):
            break
        else:
            a -= 1
            b += 1

    print(a, b)
