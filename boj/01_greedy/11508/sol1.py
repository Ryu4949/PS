n = int(input())
milk = []
for _ in range(n):
    milk.append(int(input()))
milk.sort(reverse=True)

total = sum(milk)
for i in range(n):
    if i % 3 == 2:
        total -= milk[i]

print(total)