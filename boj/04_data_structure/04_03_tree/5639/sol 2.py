import sys
sys.setrecursionlimit(10 ** 6)
num_list = []

def postorder(start, end):
    if start > end:
        return

    root = num_list[start]

    mid = end + 1

    for i in range(start + 1, end + 1):
        if root < num_list[i]:
            mid = i
            break

    postorder(start + 1, mid - 1)
    postorder(mid, end)
    print(num_list[start])

while True:
    try:
        num = int(input())
        num_list.append(num)
    except:
        break

postorder(0, len(num_list) - 1)