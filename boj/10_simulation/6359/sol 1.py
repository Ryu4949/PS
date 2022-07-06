import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    jails = [0] * (N+1) #0이면 잠겨있고, 1이면 열려있다
    rnd = 1

    while rnd <= N:
        for i in range(1, N+1):
            if i%rnd == 0:
                jails[i] = 1-jails[i]
        rnd += 1

    print(sum(jails))