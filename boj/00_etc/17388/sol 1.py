score = list(map(int, input().split()))
universities = ["Soongsil", "Korea", "Hanyang"]

if sum(score) >= 100:
    print("OK")
else:
    print(universities[min(list(enumerate(score)), key=lambda x: x[1])[0]])