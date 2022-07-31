N = int(input())
members = []
for i in range(N):
    age, name = input().split()
    members.append((i, int(age), name))

members.sort(key=lambda x: (x[1], x[0]))

for member in members:
    print(member[1], member[2])