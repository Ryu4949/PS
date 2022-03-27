from itertools import combinations
L, C = map(int, input().split())
cons = []
vowels = []
alpha = list(input().split())
for i in alpha:
    if i in 'aeiou':
        vowels.append(i)
    else:
        cons.append(i)

rlt = []

for c in range(2, C):
    v = L-c
    #고를 자음의 개수가 전체 자음의 종류 수보다 크거나
    #고를 모음의 개수가 전체 모음의 종류 수보다 크거나
    #고를 모음의 개수가 1보다 작으면 스킵
    if c > len(cons) or v > len(vowels) or v < 1:
        continue

    cons_comb = list(combinations(cons, c))
    vows_comb = list(combinations(vowels, v))

    for i in cons_comb:
        for j in vows_comb:
            word = list(i+j)
            word.sort()
            rlt.append(word)

rlt.sort()
for i in rlt:
    for j in i:
        print(j, end='')
    print()
