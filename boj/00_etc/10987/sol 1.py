word = input()
answer = 0

for i in word:
    if i in 'aeiou':
        answer += 1

print(answer)