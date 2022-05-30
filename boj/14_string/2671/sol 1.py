import re

p = re.compile('(100+1+|01)+')
code = input()
m = p.fullmatch(code)

if m:
    print("SUBMARINE")
else:
    print("NOISE")