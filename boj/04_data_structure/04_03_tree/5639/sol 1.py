data = []
while True:
    try:
        data.append(int(input()))
    except:
        break

root = data[0]
height = 1
for i in range(len(data)-1):
    if data[i+1] < data[i]:
        height += 1
    else:
        break

tree = [[0] * 3 for _ in range()]