import sys

sys.stdin = open('input.txt', encoding='utf-8')

for _ in range(1, 11):
    t = int(input())
    p = input()
    sentence = input()

    cnt = 0
    for i in range(len(sentence) - len(p) + 1):
        if p == sentence[i:i + len(p)]:
            cnt += 1

    print(f'#{t} {cnt}')
