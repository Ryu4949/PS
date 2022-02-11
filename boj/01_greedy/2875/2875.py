import math
n, m, k = map(int, input().split())
#현재 최대 가능 커플 수 = min(n//2, m)
c = min(n//2, m)

#최종가능한 커플 수를 담아줄 변수
couple = 0

#남2 여1이므로, 최대 커플을 만들고 남는 인원 수를 알 수 있음
#우선은 그 남는 인원에서 빼주고, 더 빼줘야 할 인원이 있다면 (남2, 여1)을 기준으로 빼주면 됨
if k <= (n+m) - 3*c:
    couple = c
else:
    couple = c - math.ceil((k-(n+m-3*c))/3)

print(couple)