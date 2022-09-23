A, B = map(int, input().split())
dmg = A * (100-B) /100
print(0 if dmg >= 100 else 1)