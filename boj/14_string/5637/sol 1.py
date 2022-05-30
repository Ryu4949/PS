import re

p = re.compile('[a-zA-Z-]+')
longest = ''
while True:
    sentence = input()
    m = p.findall(sentence)

    for i in m:
        if len(i) > len(longest):
            longest = i

    if m and m[-1] == 'E-N-D':
        break

print(longest.lower())