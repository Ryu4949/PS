n, k = map(int, input().split())
m = []
count = 0

for i in range(n):
    m.append(int(input()))

m.sort(reverse = True)

#화폐단위 큰 것부터
for i in m:
    #거스름돈을 모두 처리하면 반복 종료
    if k == 0: 
        break

    #거스름돈을 화폐단위로 나눈 몫만큼 개수에 더해주고, 돈은 해당 화폐단위로 나눈 나머지만 남도록
    count += k // i
    k %= i

print(count)
