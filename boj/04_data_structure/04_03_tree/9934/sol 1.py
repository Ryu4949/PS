'''
문제를 읽어보면 중위순회에 대한 문제라는 것을 알 수 있다
입력은 원래의 트리를 중위순회 한 결과
중위순회한 결과를 어떻게 원상복구 시킬 것인가?

일단 총 개수를 세고
1+2+4+ 이렇게 분해해봄
만약 총 10개라면
1+2+4+(2+1) 이렇게 될텐데
그러면 최대 레벨 3이고, 레벨 3인 노드는 3개 있다는 것
'''

N = int(input())
data = list(map(int, input().split()))
total = len(data)

lv = 0
last = 0
while True:
    if 2 ** lv - 1 >= total:
        last = total - (2 ** lv - 1)
        break
    else:
        lv += 1

print(last)