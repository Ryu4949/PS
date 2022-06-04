from collections import defaultdict
import sys
input = sys.stdin.readline

people = defaultdict(int)
N, M = map(int, input().split())
for _ in range(N):
    people[input().rstrip()] += 1

for _ in range(M):
    people[input().rstrip()] += 1

ppl_list = []
for i in people:
    if people[i] == 2:
        ppl_list.append(i)

ppl_list.sort()
print(len(ppl_list))
for i in ppl_list:
    print(i)
