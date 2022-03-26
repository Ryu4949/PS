import sys
input = sys.stdin.readline

def same(arr):
    base = arr[0][0]
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] != base:
                return False
    return True

def paper(arr):
    if same(arr):
        cnt[arr[0][0]] += 1
        return

    third = len(arr)//3

    div1 = [arr[i][:third] for i in range(third)]
    div2 = [arr[i][third:third * 2] for i in range(third)]
    div3 = [arr[i][third*2:] for i in range(third)]

    div4 = [arr[i][:third] for i in range(third, third*2)]
    div5 = [arr[i][third:third * 2] for i in range(third, third*2)]
    div6 = [arr[i][third * 2:] for i in range(third, third*2)]

    div7 = [arr[i][:third] for i in range(third*2, len(arr))]
    div8 = [arr[i][third:third * 2] for i in range(third*2, len(arr))]
    div9 = [arr[i][third*2:] for i in range(third*2, len(arr))]

    paper(div1)
    paper(div2)
    paper(div3)
    paper(div4)
    paper(div5)
    paper(div6)
    paper(div7)
    paper(div8)
    paper(div9)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = [0, 0, 0]

paper(arr)

print(cnt[-1])
print(cnt[0])
print(cnt[1])