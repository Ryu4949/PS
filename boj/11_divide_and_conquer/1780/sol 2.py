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

    for i in range(3):
        for j in range(3):
            div = [arr[k][third*i:third*(i+1)] for k in range(third*j, third*(j+1))]
            paper(div)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = [0, 0, 0]

paper(arr)

print(cnt[-1])
print(cnt[0])
print(cnt[1])