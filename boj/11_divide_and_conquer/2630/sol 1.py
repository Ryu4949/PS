def same_color(arr):
    color = arr[0][0]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] != color:
                return False
    return True

def paper(arr):
    if same_color(arr):
        cnt[arr[0][0]] += 1
        return

    half = len(arr) // 2

    left_up = [arr[i][:half] for i in range(half)]
    right_up = [arr[i][half:] for i in range(half)]
    left_down = [arr[i][:half] for i in range(half, len(arr))]
    right_down = [arr[i][half:] for i in range(half, len(arr))]

    paper(left_up)
    paper(right_up)
    paper(left_down)
    paper(right_down)

    #이 return은 꼭 필요한가?
    return

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

cnt = [0, 0]

paper(data)

print(cnt[0])
print(cnt[1])