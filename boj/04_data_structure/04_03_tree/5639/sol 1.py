from pprint import pprint

data = []
while True:
    try:
        data.append(int(input()))
    except:
        break

root = data[0]

left_tree = []
right_tree = []
for i in range(len(data)):
    if data[i] <= root:
        left_tree.append(data[i])
    else:
        right_tree.append(data[i])

print(f'left: {left_tree}')
print(f'right: {right_tree}')


'''
전위순회 결과에서 첫번째 값이 루트노드
오른쪽으로 가면서부터 왼쪽 서브트리고, 루트노드보다 큰값이 나오는 순간부터 오른쪽 서브트리
다시 각 서브트리에서 첫번째 값이 서브트리의 루트노드
... 이렇게 재귀적으로 반복
자식노드가 없어질 때까지
그게 5가 왼쪽 서브트리의 루트노드가 될 때인데

후위 순회는 왼 -> 오 -> 부모노드니까
그러면 5를 출력하고 오른쪽 28을 출력하고
그 위로 올라가서 부모노드 24출력, 
그 다음에 오른쪽 서브트리(루트노드 45)에 대해서 반복
그 다음에 부모노드 30 출력하고 오른쪽 서브트리인 98에 대해서 반복
마지막으로 루트노드 50 출력
'''


def post(start, end):
    if start > end:
