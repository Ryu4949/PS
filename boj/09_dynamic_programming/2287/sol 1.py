from collections import defaultdict
K = int(input())
N = int(input())
for _ in range(N):
    a = int(input())
    num_list = defaultdict(set)
    num_list[1] = {K}

    for i in range(2, 9):
        num_list[i].add(int(str(K) * i))

    for i in range(1, 8):
        for j in range(1, 8):
            if i + j > 8:
                continue

            for k in num_list[i]:
                for l in num_list[j]:
                    num_list[i+j].add(k+l)
                    num_list[i+j].add(abs(k-l))
                    num_list[i+j].add(k*l)
                    if l != 0:
                        num_list[i+j].add(k//l)

    for i in range(1, 9):
        if a in num_list[i]:
            print(i)
            break
    else:
        print("NO")