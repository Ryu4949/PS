import heapq

a = [1, 9, 3, 4, 5, 6, 7, 3, 1]
heapq.heapify(a)

for i in range(9):
    print(a[i])