def solution(routes):
    routes.sort(key=lambda x: x[1])
    check = []
    print(routes)
    check.append(routes[0][1])
    for i in range(1, len(routes)):
        j = check.pop()
        if routes[i][0] <= j:
            check.append(j)
        else:
            check.append(j)
            check.append(routes[i][1])
        print(check)

    return len(check)

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))

'''
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)
테스트 3 〉	통과 (0.02ms, 10.2MB)
테스트 4 〉	통과 (0.03ms, 10.1MB)
테스트 5 〉	통과 (0.03ms, 10.3MB)
효율성  테스트
테스트 1 〉	통과 (0.52ms, 10.3MB)
테스트 2 〉	통과 (0.55ms, 10.2MB)
테스트 3 〉	통과 (1.22ms, 10.6MB)
테스트 4 〉	통과 (0.09ms, 10.1MB)
테스트 5 〉	통과 (1.41ms, 10.3MB)
'''