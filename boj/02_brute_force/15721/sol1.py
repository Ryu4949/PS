#n회차 문장에는 '뻔'과 '데기'가 각각 n+3번씩 있음
#사람의 위치는 전체 수에서 사람수로 나눈 나머지

a = int(input())
t = int(input())
n = int(input())

i = 1
loop = 0
while True:
    loop += i+3
    if t <= loop:
        break
    i += 1

loop -= i+3
t -= loop

if t <= 2:
    if n == 0:
        loop += 2 *