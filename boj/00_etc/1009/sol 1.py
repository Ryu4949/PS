T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    computer = (a**b)%10
    print(computer if computer else 10)
