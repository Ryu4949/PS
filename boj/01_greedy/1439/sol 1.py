#전체 문자열에서 0의 덩어리 개수, 1의 덩어리 개수를 센 다음에 더 숫자가 적은 쪽을 출력하면 된다

S = input()
cnt = [0, 0]

last = None
for i in S:
    if i != last:
        last = i
        cnt[int(i)] += 1

print(min(cnt))