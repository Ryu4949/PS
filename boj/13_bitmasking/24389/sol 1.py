N = int(input())
MASK = 0xFFFFFFFF

a_bin = bin(N & MASK)[2:].zfill(32)
b_bin = bin(-N & MASK)[2:].zfill(32)

cnt = 0
for i in range(32):
    if a_bin[i] != b_bin[i]:
        cnt += 1

print(cnt)