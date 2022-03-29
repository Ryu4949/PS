import time
start = time.time()

rlt1 = [list(map(int, input().split())) for _ in range(71)]


print("time:", time.time() - start)

start2 = time.time()
rlt2 = [[*map(int, input().split())] for _ in 'a'*71]

print("time:", time.time()-start2)
