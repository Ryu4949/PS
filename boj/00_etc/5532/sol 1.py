L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

K = A//C+1 if A%C else A//C
M = B//D+1 if B%D else B//D

print(L-max(K, M))