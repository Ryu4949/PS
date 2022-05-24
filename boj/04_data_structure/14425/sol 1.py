from collections import defaultdict
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
str_dict = defaultdict(int)
for _ in range(N):
    str = input().rstrip()
    str_dict[str] += 1

answer = 0
for _ in range(M):
    check = input().rstrip()
    if str_dict[check] > 0:
        answer += 1

print(answer)
