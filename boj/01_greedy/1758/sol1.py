n = int(input())
tip = []
for _ in range(n):
    tip.append(int(input()))

tip.sort(reverse=True)

total = 0
for i in range(n):
    if tip[i]-i >= 0:
        total += tip[i]-i

print(total)