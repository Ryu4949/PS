'''
1번 오리가 3번땅을 갖고 싶다고 하자
먼저 3번땅을 체크해서 소유한 오리가 있는지 보고
없으면 3//2 = 1번땅으로
1번땅도 없으면 가질 수 있다
3번땅을 1번 오리가 가진 상태에서 2번오리가 6번땅을 원한다고 하자
6번땅은 비어있으니까 가능 그 다음은 6//2 = 3번땅인데
3번땅은 1번오리가 가지고 있으니까 불가능
경로를 따로 저장하면 되겠다'''

N, M = map(int, input().split())
duck = []
for _ in range(M):
    duck.append(int(input()))
tree = [1] * (N+1)

def can_get(v):
    path = []
    n = v
    while n > 0:
        path.append(n)
        n //= 2
    for i in path[::-1]:
        if not tree[i]:
            return i
    else:
        tree[v] = 0
        return 0

for i in duck:
    print(can_get(i))