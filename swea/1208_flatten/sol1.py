#상자의 높이는 1이상 100이하
#우선 주어진 데이터를 정렬
# import sys
# sys.stdin = open('input.txt')


for num in range(1, 11):
    n = int(input())
    boxes = list(map(int, input().split()))
    #상자의 개수를 담아줄 리스트
    cnt_box = [0] * 101
    for i in boxes:
        cnt_box[i] += 1
    
    #i는 0번부터 즉 최소 높이 상자의 위치, j는 끝번호 부터 즉 최대 높이 상자의 위치
    i = 0
    j = 100
    
    #cnt는 덤프 횟수
    cnt = 0
    while cnt < n:
        #현재 위치에 상자가 없다면 i는 오른쪽으로, j는 왼쪽으로 이동
        if cnt_box[i] == 0:
            i += 1
        elif cnt_box[j] == 0:
            j -= 1
        #현재 위치에 모두 상자가 있다면, i위치에서 1을 빼서 오른쪽 카운트에 1을 더해줌
        #j는 현재 위치에서 1을 빼서 왼쪽에 1을 더해줌
        #횟수 1추가하고 횟수가 n과 같아지면 반복 종료
        else:
            cnt_box[i] -= 1
            cnt_box[i+1] += 1
            cnt_box[j] -= 1
            cnt_box[j-1] += 1
            cnt += 1

    print(f'#{num} {j-i}')
