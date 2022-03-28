'''
6개씩 묶음으로 살 때 최소가격과
낱개로 살 때 최소 가격
'''

N, M = map(int, input().split())
package = []
idv = []
for _ in range(M):
    a, b = map(int, input().split())
    package.append(a)
    package.append(b*6)
    idv.append(b)

price = 0
price += (N//6) * min(package)
price += min((N%6) * min(idv), min(package))
print(price)
