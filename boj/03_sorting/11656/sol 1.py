word = input()
suffix = set()
N = len(word)

for i in range(N):
    suffix.add(word[i:])

suffix_list = sorted(list(suffix))

for sfx in suffix_list:
    print(sfx)
