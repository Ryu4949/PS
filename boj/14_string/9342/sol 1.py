import re

p = re.compile("^[A-F]?A+F+C+[A-F]?$")

N = int(input())
for _ in range(N):
    word = input()
    if p.match(word):
        print("Infected!")
    else:
        print("Good")