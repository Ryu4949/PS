#n을 입력받아 주고 리스트로 바꾼 뒤 내림차순 정렬
n = input()
num_list = list(n)
num_list.sort(reverse=True)

#정수 n이 3의 배수이고, 0이 하나라도 들어있다면 내림차순한 리스트를 하나로 합쳐서 출력
if int(n) % 3 == 0 and '0' in n:
    print(''.join(num_list))
else:
    print(-1)



