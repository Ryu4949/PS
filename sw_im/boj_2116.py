n = int(input())
dice_list = []
for _ in range(n):
    dice_list.append(list(map(int, input().split())))
pair_index = {0:5, 1:3, 2:4, 3:1, 4:2, 5:0}
result = 0

def max_dice(down, up):
    for i in range(6, 0, -1):
        if down != i and up != i:
            return i

for i in range(6):
    sum_dice = 0
    down_side = dice_list[0][i]
    up_side = dice_list[0][pair_index[i]]
    sum_dice += max_dice(down_side, up_side)
    
    for j in range(1, n):
        down_side = up_side
        up_side = dice_list[j][pair_index[dice_list[j].index(down_side)]]
        sum_dice += max_dice(down_side, up_side)
    
    if sum_dice > result:
        result = sum_dice

print(result)