n, m = map(int, input().split())
card = list(map(int, input().split()))

sum_card = 0
a = len(card)

for i in range(0, a - 2):
  for j in range(i + 1, a - 1):
    for k in range(j + 1, a):
      if card[i] + card[j] + card[k] > m:
        continue
      else:
        sum_card = max(sum_card, card[i] + card[j] + card[k])

print(sum)