import re

N = int(input())
start, end = input().split('*')
p = re.compile('^'+start+'.*'+end+'$')
for _ in range(N):
    file_name = input()
    if p.match(file_name):
        print("DA")
    else:
        print("NE")