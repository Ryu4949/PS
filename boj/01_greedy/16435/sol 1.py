N, L = map(int, input().split())
fruits = [*map(int, input().split())]
fruits.sort()

snake = L
for i in fruits:
    if i <= snake:
        snake += 1
    else:
        break

print(snake)