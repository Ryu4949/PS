import re

p = re.compile('pi|ka|chu')

pikachu = input()

if len(''.join(p.findall(pikachu))) == len(pikachu):
    print("YES")
else:
    print("NO")