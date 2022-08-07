N = int(input())
problems = []
for _ in range(N):
    a, b = input().split()
    problems.append((a, int(b)))

print(min(problems, key=lambda x: x[1])[0])