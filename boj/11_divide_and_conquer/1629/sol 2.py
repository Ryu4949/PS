#시간초과 풀이
#이 경우 b가 짝수인지 홀수인지 나눌 필요는 없어졌지만
#함수를 중복되게 호출하는 경우가 많아서 시간초과가 발생하는 것 같다

A, B, C = map(int, input().split())
def mod(a, b, c):
    if b == 1:
        return (a ** b) % c

    else:
        return (mod(a, b // 2, c) * mod(a, b - b//2, c)) % c

print(mod(A, B, C))