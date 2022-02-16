t = int(input())
for num in range(1, t + 1):
    n = int(input())


    def itoa(n):
        # 빈문자열 생성
        result = ''

        # n이 양수라면 아무런 조치 없음
        if n >= 0:
            sign = ''

        # n이 음수라면 sign은 문자열 -이고, n에 -1을 곱해줌
        else:
            sign = '-'
            n *= -1

        # 아스키코드와 10의 나머지 연산을 활용하여 n의 끝자리부터 문자열로 빈문자열에 합침
        # 마지막에는 result를 역순으로 한 것과 sign을 합쳐서 반환
        while n != 0:
            result += chr((n % 10) + 48)
            n //= 10
        return sign + result[::-1]


    print(f'#{num} {itoa(n)} {type(itoa(n))}')