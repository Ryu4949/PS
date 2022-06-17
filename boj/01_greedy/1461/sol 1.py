import sys
input = sys.stdin.readline

N, M = map(int, input().split())
books = [*map(int, input().split())]
pos = []
neg = []
for book in books:
    if book > 0:
        pos.append(book)
    else:
        neg.append(book)

pos.sort(reverse=True)
neg.sort()

answer = 0
for i in range(0, len(pos), M):
    answer += pos[i]

for i in range(0, len(neg), M):
    answer -= neg[i]

print(answer*2-abs(max(books, key=lambda x: abs(x))))