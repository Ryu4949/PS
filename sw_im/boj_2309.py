from itertools import combinations
dwarfs = []
for _ in range(9):
    dwarfs.append(int(input()))

#가짜난쟁이 2명의 키의 합
target_sum = sum(dwarfs) - 100

#난쟁이들 중 2명의 조합을 구해서, 해당 조합의 키의 합이 target_sum과 같으면
#난쟁이 리스트에서 제거해주고 반복 종료
comb = list(combinations(dwarfs, 2))
for i in comb:
    if sum(i) == target_sum:
        for j in i:
            dwarfs.remove(j)
        break

#남은 난쟁이의 리스트를 정렬하고 출력
dwarfs.sort()
for dwarf in dwarfs:
    print(dwarf)
