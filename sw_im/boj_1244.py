n = int(input())
switches = list(map(int, input().split()))
students_num = int(input())
#학생 수만큼 반복
for _ in range(students_num):
    gen, pos = map(int, input().split())

#남학생인 경우
    if gen == 1:
        i = 1
        while pos*i - 1 <= n-1:
            switches[pos*i-1] = abs(1-switches[pos*i-1])
            i += 1

#여학생인 경우
#바꿔줘야 할 범위를 확정시키고 범위의 스위치를 일괄 교체
    else:
        start = pos-1
        end = pos-1
        k = 0
        while True: 
            if start-k < 0 or end+k >= n or switches[start-k] != switches[end+k]:
                k -= 1
                break
            k += 1
        for i in range(start-k, end+k+1):
            switches[i] = abs(1-switches[i])

#20개씩 출력
for i in range(0, n, 20):
    print(' '.join(map(str, switches[i:i+20])))