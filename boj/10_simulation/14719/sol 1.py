H, W = map(int, input().split())
block = [*map(int, input().split())]

idx = block.index(max(block))
left = block[0]
right = block[-1]

total = 0

for i in range(1, idx):
    if block[i] > left:
        left = block[i]
    else:
        total += left-block[i]

for i in range(W-1, idx, -1):
    if block[i] > right:
        right = block[i]
    else:
        total += right-block[i]

print(total)