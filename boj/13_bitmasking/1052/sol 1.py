N, K = map(int, input().split())

water = N
ans = 0
while True:
    water_bi = bin(water)[2:][::-1]
    if water_bi.count('1') <= K:
        break

    i = water_bi.index('1')
    ans += 2**i
    water += 2**i

print(ans)