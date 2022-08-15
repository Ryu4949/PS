students = [1]*31
for _ in range(28):
    n = int(input())
    students[n] = 0

for i in range(1, 31):
    if students[i] == 1:
        print(i)