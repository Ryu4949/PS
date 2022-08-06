def yut(data):
    y = ["E", "A", "B", "C", "D"]
    return y[data.count(0)]

for _ in range(3):
    data = [*map(int, input().split())]
    print(yut(data))