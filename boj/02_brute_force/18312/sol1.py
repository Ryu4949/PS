#시/분/초가 한자리일 때, 디지털시계이므로 01초 02초 등이 되어야 하는데 range에서는 그렇지 않으므로
#시+분+초 문자열의 길이가 6보다 작다면 그만큼 0을 덧붙여줌

n, k = map(int, input().split())

cnt = 0
for h in range(n+1):
    for m in range(60):
        for s in range(60):
            time = str(h) + str(m) + str(s)
            if len(time) < 6:
                time += '0' * (6-len(time))

            if str(k) in time:
                cnt += 1

print(cnt)


