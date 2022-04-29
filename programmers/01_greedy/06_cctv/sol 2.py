def solution(routes):
    answer = 1
    routes.sort(key=lambda x: x[1])
    last = routes[0][1]
    for i in range(1, len(routes)):
        if routes[i][0] > last:
            last = routes[i][1]
            answer += 1

    return answer

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))

'''
채점을 시작합니다.
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.02ms, 10.3MB)
테스트 3 〉	통과 (0.02ms, 10.1MB)
테스트 4 〉	통과 (0.02ms, 10.1MB)
테스트 5 〉	통과 (0.02ms, 10.2MB)
효율성  테스트
테스트 1 〉	통과 (0.43ms, 10.5MB)
테스트 2 〉	통과 (0.25ms, 10.3MB)
테스트 3 〉	통과 (0.84ms, 10.5MB)
테스트 4 〉	통과 (0.06ms, 10.1MB)
테스트 5 〉	통과 (1.01ms, 10.5MB)
채점 결과
정확성: 50.0
효율성: 50.0
합계: 100.0 / 100.0
'''