import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))
# num_list = list(set(lst))
lst.sort()
rlt = []
ans = []

def perm(i):
    if i == M:
        ans.append(rlt)
        return

    for j in lst:
        rlt.append(j)
        perm(i+1)
        rlt.pop()

perm(0)

print(f'ans: {ans}')
print(lst)
# print(num_list)