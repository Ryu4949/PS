#관계가 주어진다면 그래프를 떠올려보자!

N, M = map(int,input().split())
# 아이스크림간의 관계를 담는 리스트 relation
relation = [[] for _ in range(N+1)]

# relation에 정보 저장
for _ in range(M):
    a, b = map(int, input().split())
    relation[a].append(b)
    relation[b].append(a)

cnt = 0

for i in range(1,N-1):
    for j in range(i+1,N):
        for k in range(j+1,N+1):
            # 아이스크림들이 관계가 없다면
            if j not in relation[i] and k not in relation[i] and k not in relation[j]:
                cnt += 1

print(cnt)