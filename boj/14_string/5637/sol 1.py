import re

p = re.compile('[a-zA-Z]*-*', re.MULTILINE)
sentence = input()
m = p.findall(sentence)
print(m)
