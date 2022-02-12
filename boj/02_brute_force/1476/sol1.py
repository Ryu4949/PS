e, s, m = map(int, input().split())
# e: 1~15, s: 1~28, m: 1~19
# e에 기준을 맞춰서 해결(e가 제일 작으므로 e에 가능한 값은 s, m도 가능)

n = e - 1
e -= 1
s -= 1
m -= 1

ee = ss = mm = e

i = 0
while True:
    if ee == e and ss == s and mm == m:
        break

    i += 1
    ss = (ss + 15) % 28
    mm = (mm + 15) % 19

print(15 * i + n + 1)