A, B, C, M = map(int, input().split())

time = 0
tired = 0
work = 0
while True:
    time += 1
    if tired + A > M:
        tired = max(tired - C, 0)
    else:
        tired += A
        work += B

    if time == 24:
        break

print(work)