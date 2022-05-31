import re

p = re.compile('(100+1+|01)+')

N = int(input())
for _ in range(N):
    code = input()
    if p.fullmatch(code):
        print("YES")
    else:
        print("NO")