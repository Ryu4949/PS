import sys
input = sys.stdin.readline

N = int(input())
weights = [*map(int, input().split())]

weights.sort()

check = 1
for weight in weights:
    if weight > check:
        break
    check += weight

print(check)