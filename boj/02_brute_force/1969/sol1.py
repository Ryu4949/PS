#입력받은 데이터를 세로로 한묶음으로 차례대로 검토
#해당 묶음에서 가장 많은 dna 종류를 담아주고, 그 때마다 hamming에는 N-(해당 dna의 개수)만큼 더해준다.

N, M = map(int, input().split())
dna = []
for _ in range(N):
    dna.append(list(input()))

trans_dna = list(map(list, zip(*dna)))

for i in trans_dna:
    i.sort()

data = ['A', 'C', 'G', 'T']

cnt = [[0] * 4 for _ in range(M)]
for i in range(M):
    for j in range(4):
        cnt[i][j] += trans_dna[i].count(data[j])

result = ''
hamming = 0
for i in cnt:
    hamming += N - max(i)
    result += data[i.index(max(i))]

print(result)
print(hamming)